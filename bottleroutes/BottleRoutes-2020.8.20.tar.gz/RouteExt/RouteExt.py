from bottle import Bottle


class ControllersException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)


class Controllers:
    def get(self):
        return ControllersException("Method not implemented.")

    def post(self):
        raise ControllersException("Method not implemented.")

    def put(self):
        raise ControllersException("Method not implemented.")

    def delete(self):
        raise ControllersException("Method not implemented.")


def register(self, obj: Controllers):
    if not issubclass(type(obj), Controllers):
        raise ControllersException(
            f"Object {type(obj)} is not subclass from Controllers."
        )
    self.route(obj.url, "GET", callback=obj.get)
    self.route(obj.url, "POST", callback=obj.post)
    self.route(obj.url, "PUT", callback=obj.put)
    self.route(obj.url, "DELETE", callback=obj.delete)


def set_controller_handler(app: Bottle):
    setattr(app, "register", register)
    return app()
