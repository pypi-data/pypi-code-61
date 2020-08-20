from meinheld import server
from werkzeug.debug import DebuggedApplication
from werkzeug._reloader import run_with_reloader

from .util import logger
from .util import load_app


def debug(app_path, host, port):

    def capture(request, response):
        logger.exception('internal server error', stack_info=True)

    app, _ = load_app(app_path)
    app.on('capture', capture)
    app.on('log', lambda method, *a, **kw: getattr(logger, method)(*a, **kw))

    def _run():
        server.listen((host, int(port)))
        logger.info(f' * Fermata on: http://{host}:{port}')
        server.run(DebuggedApplication(app, evalex=True))

    run_with_reloader(_run, app.spec_files)
