from functools import wraps
from flask import g, request, jsonify
from path import join, dirname
from furl import furl
import stripe

PAYMENT_STATE_KEY = "_lonny_flask_payments"
PROTO_HEADER = "X-Forwarded-Proto"
ASSET_PATH = join(dirname(__file__), "transit.html")

class PaymentState:
    def __init__(self):
        self.success = False

def _get_payment_state():
    g.setdefault(PAYMENT_STATE_KEY, PaymentState())

def is_success():
    return get_payment_state().success

class StripeStrategy:
    def __init__(self, stripe_secret_key, stripe_public_key):
        self._stripe_public_key = stripe_public_key
        with open(ASSET_PATH) as f:
            self._asset_templ = f.read()
        stripe.api_key = stripe_secret_key

    def __call__(self, fn):
        @wraps(fn)
        def wrapped(*args, **kwargs):
            if "status" not in request.args:
                session_id = self._setup_session()
                return self.handle_session(session_id)
            if request.args["status"] == "success":
                self._attach_payment_method(request.args["session_id"])
                _get_payment_state().success = True
            fn(*args, **kwargs)
        return wrapped

    def update_payment_method(self, customer_id, payment_method_id):
        raise NotImplementedError()

    def get_customer_id(self):
        raise NotImplementedError()
    
    def handle_session(self, session_id):
        return jsonify(session_id = session_id)

    def _attach_payment_method(self, session_id):
        session = stripe.checkout.Session.retrieve(session_id)
        setup_intent = stripe.SetupIntent.retrieve(session["data"]["object"]["setup_intent"])
        stripe.PaymentMethod.attach(
            setup_intent["payment_method"],
            customer = setup_intent["customer"]
        )
        self.update_payment_method(setup_intent["customer"], setup_intent["payment_method"]

    def _setup_session(self):
        new_scheme = request.headers.get(PROTO_HEADER, request.scheme)
        parsed = furl(request.url).set(scheme = new_scheme)
        session = stripe.checkout.Session.create(
            payment_method_types = ["card"],
            mode = "setup",
            customer = self.get_customer_id(),
            success_url = furl(parsed).set(args = dict(status = "success", session_id = "{CHECKOUT_SESSION_ID}")),
            cancel_url = furl(parsed).set(args = dict(status = "cancel"))
        )
        return session["id"]