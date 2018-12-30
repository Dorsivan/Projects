from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import Views


def main():
        config = Configurator()
        config.add_route('upload', '/upload')  # upload data to DB and send to task queue
        config.add_route('getresult', '/results/{id}')  # get the result for id from the DB
        config.add_view(Views.upload, route_name='upload', request_method='POST', renderer='string')
        config.add_view(Views.getresult, route_name='getresult', request_method='GET')
        app = config.make_wsgi_app()
        return app


Base = declarative_base()


class datarow(Base):  # row in the DB
    __tablename__ = 'client_data'  # table name
    id = Column(Integer, primary_key=True)
    rawData = Column(String)
    result = Column(Integer)


def init_db():
    engine = create_engine('sqlite:///tasks.db', echo=True)  # create DB
    Base.metadata.create_all(bind=engine)
    Session = sessionmaker(bind=engine)
    session = Session()


if __name__ == '__main__':
    app = main()
    init_db()
    server = make_server('0.0.0.0', 4555, app)
    server.serve_forever()




