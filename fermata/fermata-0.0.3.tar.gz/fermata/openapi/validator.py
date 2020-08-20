import json
from urllib.parse import parse_qs

from . import jsonschema
from ..exception import VerificationFailed

CONTENT_NAME = 'body'


class FormDeserializer:

    def __init__(self, schema, encoding):
        self.encoding = encoding
        self.properties = {}
        for p, s in schema.get('properties', {}).items():
            type_ = s.get('items', s).get('type')
            self.properties[p] = {
                'multi': 'items' in s,
                'deserializer': DESERIALIZERS.get(type_)
            }

    def __call__(self, content: bytes):
        result = {}
        data = parse_qs(content)
        for p, clause in self.properties.items():
            multi = clause['multi']
            deserializer = clause['deserializer']
            try:
                result[p] = (next, list)[int(multi)](
                    deserializer(d) for d in data[p])
            except KeyError:
                continue
        return result

DESERIALIZERS = {
    'integer': int,
    'string': str,
    'number': float,
    'bool': lambda x: x in ('true', 'True'),
}

DESERIALIZERS_LIST = {
    'integer': lambda l: [int(v) for v in l],
    'string': lambda l: [str(v) for v in l],
    'number': lambda l: [float(v) for v in l],
    'bool': lambda l: [v in ('true', 'True') for v in l],
}

DESERIALIZERS_CONTENT = {
    'application/json': lambda schema, encoding: json.loads,
    'application/x-www-form-urlencoded': FormDeserializer,
}


def build_clause(param):
    location, name, required, schema = (
        param.get('in'),
        param.get('name'),
        param.get('required', False),
        param.get('schema', {}),
    )
    if not location or not name:
        return None

    # match request.attr
    location = {
        'query': 'params',
        'path': 'sections',
        'header': 'headers',
    }.get(location, location)

    # required no defaults
    default = None if required else schema.get('default', None)

    # > items MUST be present if the type is array.
    multi = 'items' in schema
    type_ = schema.get('items', schema).get('type')

    # type convert
    deserializer = (DESERIALIZERS, DESERIALIZERS_LIST)[int(multi)].get(type_)
    if 'content' in param:
        for content_type, node in param['content'].items():
            try:
                cls = DESERIALIZERS_CONTENT[content_type]
            except KeyError:
                # TODO: warning on console
                break
            schema = node.get('schema')
            encoding = node.get('encoding')
            # <Media Type Object>.encoding
            # need_encode = (content_type.startswith('multipart/') or 
            #     content_type == 'application/x-www-form-urlencoded')
            deserializer = cls(schema, encoding)
            break  # only one content type will be use

    # validator
    validator = jsonschema.create(schema) if schema else None

    return {
        'location': location,
        'name': name,
        'multi': multi,
        'required': required,
        'default': default,
        'type_': type_,
        'deserializer': deserializer,
        'validator': validator,
    }


def content_clause(content_type, param, required):
    '''
       :content_type: str
       :param: operation.requestBody.content[content_type] <Media Type Object>
    '''
    return build_clause({
        'required': required,
        'in': 'content',
        'name': CONTENT_NAME,
        'content': {
            content_type: {
                'schema': param.get('schema'),
                'encoding': param.get('encoding'),
            }
        }
    })


class Validator:

    def __init__(self, parameters, content, content_required=False):
        clauses = [build_clause(p) for p in parameters]
        self.clauses = [c for c in clauses if c]
        self.content_clauses = {}
        self.content_required = content_required
        for media, data in content.items():
            c = content_clause(media, data, content_required)
            if c:
                self.content_clauses[media] = c

    def _clauses(self, request):
        t = request.content_type or 'application/json'
        c = self.content_clauses.get(t) or self.content_clauses.get('*/*')
        if self.content_required and not c:
            c = { 'in': 'content', 'name': CONTENT_NAME, 'required': True}
        return self.clauses + ([c] if c else [])

    def validate(self, request):
        params, errors = {}, []

        for clause in self._clauses(request):
            location = clause['location']
            name = clause['name']
            multi = clause['multi']
            default = clause['default']
            required = clause['required']

            data = getattr(request, location)
            if location == 'content':
                exist = len(data) > 0
            else:
                exist = name in data

            if location == 'content':
                value = data
            elif multi:
                value = data.get_list(name)
            else:
                value = data.get(name)

            # deserialize
            deserializer = clause['deserializer']
            if exist and deserializer:
                try:
                    value = deserializer(value)
                except ValueError:
                    errors.append(dict(name=name, value=value, message='type convert error'))

            # required and default
            if required and not exist:
                errors.append(dict(
                        name=name, 
                        message=f'var {name} in {location} is required'))
            elif default and not exist:
                exist, value = True, default

            # validate
            validator = clause['validator']
            if exist:
                if validator:
                    for e in validator.iter_errors(value):
                        errors.append(dict(name=name, value=value, message=e.message))
            elif required:
                errors.append(dict(name=name, message=f'{name} in {location} is required'))

            # store
            if exist:
                params[name] = value

        if errors:
            raise VerificationFailed(errors)

        return params
