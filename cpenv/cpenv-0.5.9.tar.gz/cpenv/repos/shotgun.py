# -*- coding: utf-8 -*-
# Standard library imports
import io
import fnmatch
import os
import zipfile
from functools import partial

# Third party imports
try:
    import certifi
except ImportError:
    from ..vendor import certifi

# Local imports
from .. import http, paths
from ..module import Module, ModuleSpec, parse_module_requirement, sort_modules
from ..reporter import get_reporter
from ..vendor import yaml
from ..vendor.shotgun_api3 import Shotgun
from ..vendor.cachetools import TTLCache, cachedmethod, keys
from ..versions import parse_version
from .base import Repo


class ShotgunRepo(Repo):
    '''Use Shotgun's database as a Repo for modules.

    Requirements:
        A CustomNonProjectEntity named "Module" to be enabled via
        Shotgun site-preferences with the following fields enabled:

        The following fields must be added to the "Module" entity.
          - archive       File/Link
          - archive_size  Number
          - author        Text
          - description   Text
          - email         Text
          - version       Text

        A CustomEntity named "Environment" to be enabled via
        Shotgun site-preferences with the following fields enabled:
          - engine        Text
          - requires      Text

    Arguments:
        name (str): Name of this Repo
        module_entity (str): Name of Module entity (CustomNonProjectEntity01)
        base_url (str): Path to Shotgun site (https://my.shotgunstudio.com)
        script_name (str): Name of Shotgun api script
        api_key (str): Key of Shotgun api script
        api (Shotgun): shotgun_api3.Shotgun instance

    Examples:
        >>> from shotgun_api3 import Shotgun
        >>> sg = Shotgun(base_url, script_name, api_key)
        >>> ShotgunRepo('MyShotgunRepo', api=sg)

        OR

        >>> ShotgunRepo('MyShotgunRepo', base_url, script_name, api_key)
    '''

    type_name = 'shotgun'

    def __init__(
        self,
        name,
        base_url=None,
        script_name=None,
        api_key=None,
        api=None,
        module_entity='CustomNonProjectEntity01',
    ):
        super(ShotgunRepo, self).__init__(name)
        if api:
            # Assume we've received a Shotgun instance
            # This will be done via the tk-cpenv shotgun app
            self._api = api
        else:
            self._api = Shotgun(
                base_url=base_url,
                script_name=script_name,
                api_key=api_key,
                ca_certs=certifi.where(),
            )

        self.base_url = self._api.base_url
        self.path = self._api.base_url
        self.module_entity = module_entity
        self.resolve_fields = ['code', 'sg_version']
        self.data_fields = [
            'code',
            'sg_version',
            'description',
            'sg_author',
            'sg_email',
            'sg_data',
        ]
        self.archive_fields = ['sg_archive', 'sg_archive_size']
        self.cache = TTLCache(maxsize=10, ttl=60)

    @property
    def shotgun(self):
        return self._api

    def clear_cache(self):
        self.cache.clear()

    @cachedmethod(lambda self: self.cache, key=partial(keys.hashkey, 'find'))
    def find(self, requirement):
        name, version = parse_module_requirement(requirement)

        # Build filters
        filters = [['code', 'is', name]]
        exact_filters = list(filters)
        if version:
            exact_filters.append(['sg_version', 'is', version.string])

        # Try exact match first
        entities = self.shotgun.find(
            self.module_entity,
            filters=exact_filters,
            fields=self.resolve_fields,
        )
        if not entities:
            # Fall back to simple name match
            entities = self.shotgun.find(
                self.module_entity,
                filters=filters,
                fields=self.resolve_fields,
            )

        module_specs = []
        for entity in entities:
            module_specs.append(entity_to_module_spec(entity, self))

        return sort_modules(module_specs, reverse=True)

    @cachedmethod(lambda self: self.cache, key=partial(keys.hashkey, 'list'))
    def list(self):
        entities = self.shotgun.find(
            self.module_entity,
            filters=[],
            fields=self.resolve_fields,
        )
        module_specs = []
        for entity in entities:
            module_specs.append(entity_to_module_spec(entity, self))

        return sort_modules(module_specs, reverse=True)

    def download(self, module_spec, where, overwrite=False):

        entity = self.shotgun.find_one(
            self.module_entity,
            filters=module_spec_to_filters(module_spec),
            fields=self.archive_fields,
        )
        archive = entity['sg_archive']

        if not archive:
            print('Module entity has no associated archive.')
            return

        if os.path.isdir(where):
            if overwrite:
                paths.rmtree(where)
            else:
                raise Exception('Module already exists in download location.')

        # Download archive data - we add a chunk to download_size for zip
        # progress reporting.
        reporter = get_reporter()
        chunk_size = 8192
        download_size = self.get_size(module_spec)
        zip_chunk_size = (download_size / chunk_size) * 10
        progress_bar = reporter.progress_bar(
            label='Download %s' % module_spec.name,
            max_size=download_size + zip_chunk_size,
            data={'module_spec': module_spec},
        )
        with progress_bar as progress_bar:
            response = http.get(archive['url'])
            data = io.BytesIO()
            while True:
                chunk = response.read(chunk_size)
                if not chunk:
                    break
                progress_bar.update(len(chunk))
                data.write(chunk)

            # Construct and extract in-memory zip archive
            zip_file = zipfile.ZipFile(data)
            zip_file.extractall(where)
            progress_bar.update(zip_chunk_size)

            module = Module(where)
            progress_bar.update(data={
                'module_spec': module_spec,
                'module': module,
            })

        return module

    def upload(self, module, overwrite=False):
        from .. import api

        entity = self.shotgun.find_one(
            self.module_entity,
            filters=module_spec_to_filters(module),
            fields=self.archive_fields,
        )
        if entity:
            if overwrite:
                self.shotgun.delete(self.module_entity, entity['id'])
            else:
                raise Exception('Module already uploaded.')

        reporter = get_reporter()
        progress_bar = reporter.progress_bar(
            label='Upload %s' % module.name,
            max_size=3,
            data={'module': module, 'unit': 'iT', 'to_repo': self},
        )

        with progress_bar as progress_bar:
            # 1. Create archive
            archive = api.get_cache_path('tmp', module.qual_name + '.zip')
            zip_folder(module.path, archive)
            archive_size = os.path.getsize(archive)
            progress_bar.update(1)

            # 2. Upload archive
            data = module_to_entity(module, sg_archive_size=archive_size)
            entity = self.shotgun.create(self.module_entity, data)
            self.shotgun.upload(
                self.module_entity,
                entity['id'],
                path=archive,
                field_name='sg_archive',
            )
            progress_bar.update(1)

            # 3. Upload icon as thumbnail
            if module.has_icon():
                self.shotgun.upload_thumbnail(
                    self.module_entity,
                    entity['id'],
                    module.icon,
                )
            progress_bar.update(1)

            module_spec = entity_to_module_spec(entity, self)
            progress_bar.update(data={
                'module_spec': module_spec,
            })

        # Delete local archive
        try:
            os.unlink(archive)
        except OSError as e:
            print('Warning: failed to remove %s' % archive)
            print('         ' + str(e))

        return module_spec

    def remove(self, module_spec):
        entity = self.shotgun.find_one(
            self.module_entity,
            filters=module_spec_to_filters(module_spec),
            fields=[],
        )
        if entity:
            self.shotgun.delete(self.module_entity, entity['id'])

    def get_data(self, module_spec):
        entity = self.shotgun.find_one(
            self.module_entity,
            filters=module_spec_to_filters(module_spec),
            fields=self.data_fields,
        )
        if not entity:
            raise Exception('Failed to locate %s in %s' % (
                module_spec.qual_name,
                module_spec.repo,
            ))

        # Load module.yml data from sg_data field
        try:
            data = yaml.safe_load(entity['sg_data'])
        except Exception as e:
            print('Error: ' + e.message)
            print('Failed to load data from sg_data field.')
            data = {}

        # Fill missing data with entity level data
        data.setdefault('name', entity['code'])
        data.setdefault('version', entity['sg_version'])
        data.setdefault('author', entity['sg_author'])
        data.setdefault('email', entity['sg_email'])
        data.setdefault('description', entity['description'])
        data.setdefault('requires', [])
        data.setdefault('environment', {})

        return data

    def get_thumbnail(self, module_spec):
        from .. import api

        # We need to construct a url since the shotgun api only
        # returns a url for a low res thumbnail.
        base_url = self.base_url
        name_and_id = module_spec.path.split('/')[-2:]
        thumbnail_url = base_url + '/thumbnail/full/' + '/'.join(name_and_id)

        # Ensure icons cache dir exists
        icons_root = api.get_cache_path('icons')
        if not os.path.isdir(icons_root):
            os.makedirs(icons_root)

        # Cache thumbnail locally
        icon_path = api.get_cache_path(
            'icons',
            module_spec.qual_name + '_icon.png'
        )
        if not os.path.isfile(icon_path):
            try:
                data = self.shotgun.download_attachment(
                    {'url': thumbnail_url}
                )
                with open(icon_path, 'wb') as f:
                    f.write(data)
            except Exception:
                return

        return icon_path

    def get_size(self, spec):
        '''Query Shotgun for archive size.'''

        return int(self.shotgun.find_one(
            self.module_entity,
            filters=[
                ['code', 'is', spec.name],
                ['sg_version', 'is', spec.version.string]
            ],
            fields=['sg_archive_size'],
        )['sg_archive_size'] or 0)


def entity_to_module_spec(entity, repo):
    '''Convert entity data to a ModuleSpec.'''

    qual_name = '{code}-{sg_version}'.format(**entity)
    version = parse_version(entity['sg_version'])
    url = "{base_url}/detail/{module_entity}/{id}".format(
        base_url=repo.base_url,
        module_entity=repo.module_entity,
        id=entity['id'],
    )
    return ModuleSpec(
        name=entity['code'],
        real_name=qual_name,
        qual_name=qual_name,
        version=version,
        path=url,
        repo=repo,
    )


def module_spec_to_filters(module_spec):
    '''Convert a ModuleSpec to a list of filters used in a shotgun query.'''

    return [
        ['code', 'is', module_spec.name],
        ['sg_version', 'is', module_spec.version.string],
    ]


def module_to_entity(module, **fields):
    '''Convert a Module or ModuleSpec to data for an entity in shotgun.'''

    fields.setdefault('code', module.name)
    fields.setdefault('sg_version', module.version.string)
    fields.setdefault('description', getattr(module, 'description', ''))
    fields.setdefault('sg_author', getattr(module, 'author', ''))
    fields.setdefault('sg_email', getattr(module, 'email', ''))
    data = module.raw_config.strip('\n')
    fields.setdefault('sg_data', data)
    return fields


def zip_folder(folder, where):
    '''Zip the contents of a folder.'''

    parent = os.path.dirname(where)
    if not os.path.isdir(parent):
        os.makedirs(parent)

    # TODO: Count files first so we can report progress of building zip

    with zipfile.ZipFile(where, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, subdirs, files in paths.exclusive_walk(folder):
            rel_root = os.path.relpath(root, folder)
            for file in files:
                zip_file.write(
                    os.path.join(root, file),
                    arcname=os.path.join(rel_root, file)
                )
