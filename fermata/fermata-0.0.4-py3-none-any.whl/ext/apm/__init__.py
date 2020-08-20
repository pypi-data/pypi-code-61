from fermata import __version__
import elasticapm
from elasticapm.conf import constants

from .util import get_data_from_request
from .util import get_data_from_response

'''
ref: [Creating Custom Framework Integrations with the Elastic APM Python Agent](https://www.elastic.co/cn/blog/creating-custom-framework-integrations-with-the-elastic-apm-python-agent)
'''


class ElasticAPM:

    def __init__(self, app, **defaults):
        elasticapm.instrument()
        self.client = elasticapm.Client(
            framework_name='fermata',
            framework_version=__version__,
            **defaults)
        app.on('request', self.request)
        app.on('respond', self.respond)
        app.on('abort', self.abort)
        app.on('capture', self.capture)
        app.apm = self

    def request(self, request):
        parent = elasticapm.trace_parent_from_headers(request.headers)
        self.client.begin_transaction('request', trace_parent=parent)
        elasticapm.set_context(
            lambda: get_data_from_request(
                request, self.client.config, constants.TRANSACTION),
            "request")

    def respond(self, request, response):
        elasticapm.set_context(
            lambda: get_data_from_response(
                response, self.client.config, constants.TRANSACTION),
            "request")
        name = f'{request.operation} {request.expression}'
        result = str(response.status_code)[:1] + 'xx'
        self.client.end_transaction(name, result)

    def abort(self, request, response):
        self.respond(request, response)

    def capture(self, request, response):
        self.client.capture_exception(
            context={
                "request": get_data_from_request(
                    request, self.client.config, constants.ERROR)
            },
            handled=False)
        self.respond(request, response)

    def log(self, *args, **kwargs):
        return self.client.capture_message(*args, **kwargs)


def init(app, **defaults):
    return ElasticAPM(app, **defaults)
