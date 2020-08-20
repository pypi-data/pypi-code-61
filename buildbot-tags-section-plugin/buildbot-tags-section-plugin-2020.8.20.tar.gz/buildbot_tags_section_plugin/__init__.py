from buildbot.www.plugin import Application

# create the interface for the setuptools entry point
ep = Application(__name__, "Buildbot tags section menu plugin", ui=True)
