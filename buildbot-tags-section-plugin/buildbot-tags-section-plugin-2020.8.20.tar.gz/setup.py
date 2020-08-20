#!/usr/bin/env python

try:
    from buildbot_pkg import setup_www_plugin
except ImportError:
    import sys
    print('Please install buildbot_pkg module in order to install that '
          'package, or use the pre-build .whl modules available on pypi',
          file=sys.stderr)
    sys.exit(1)


with open("README.md", "r") as fh:
    long_description = fh.read()

setup_www_plugin(
    name='buildbot-tags-section-plugin',
    description='Add builders filters menu section',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author=u'Evgeny Vlasov',
    author_email=u'evgeny.vlasov@fruct.org',
    url='https://github.com/vlasov-evgeny/buildbot-tags-section',
    packages=['buildbot_tags_section_plugin'],
    package_data={
        '': [
            'VERSION',
            'static/*'
        ]
    },
    entry_points="""
        [buildbot.www]
        tags_section_plugin = buildbot_tags_section_plugin:ep
    """,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)'
    ],
)
