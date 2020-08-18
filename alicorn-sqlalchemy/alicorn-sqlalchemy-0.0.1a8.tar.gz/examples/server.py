from alicorn import Alicorn, Depends
from grpc import StatusCode

from alicorn_sqlalchemy import AlicornSqlAlchemy
import sqlalchemy as sa
from proto.helloworld_pb2 import *
from proto.helloworld_pb2_grpc import *
from logging import basicConfig

basicConfig()

app = Alicorn(config={
    'sqlalchemy': {
        'uri': 'sqlite:///test.db'
    }
})
app.debug = True

db = AlicornSqlAlchemy()
app.add_extension(db)


class TestModel(db.Base):
    __tablename__ = 'test_model'

    id = sa.Column(sa.Integer(), primary_key=True)
    name = sa.Column(sa.String(24))


@app.service
class HelloWorldService(HelloWorldServiceServicer):

    def SayHello(self, request: HelloWorldRequest, context, session: db.Session=Depends(db.get_session)) -> HelloWorldResponse:
        model = session.query(TestModel).filter(TestModel.name == request.name).first()
        if not model:
            context.set_code(StatusCode.NOT_FOUND)
            return HelloWorldResponse()

        return HelloWorldResponse(message=f"Hello {model.name}")


if __name__ == '__main__':
    app.run()
