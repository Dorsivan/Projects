import TaskApi
import TaskQueue
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pyramid.response import Response


def upload(request):
    # DB connection
    engine = create_engine('sqlite:///tasks.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # decode json body
    json_data = json.loads(json.dumps(request.json_body))
    for temp in json_data:
        datarow = TaskApi.datarow()
        datarow.id = int(temp)
        datarow.rawData = str(json_data[temp])
        datarow.result = None
        session.add(datarow)

    session.commit()  # commit all changes to DB
    session.close()

    TaskQueue.mul.delay()  # tells TaskQueue to calculate the results for the added rows


def getresult(request):
    # DB connection
    engine = create_engine('sqlite:///tasks.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    reqid = request.matchdict['id']  # the required id from the request
    foundrow = session.query(TaskApi.datarow).get(reqid)  # filter the rows in db by id
    session.close()
    return Response('{"result":' + str(foundrow.result) + '}')  # returns the result of the row with the required id
