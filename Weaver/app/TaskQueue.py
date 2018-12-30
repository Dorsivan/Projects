import TaskApi
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from celery import Celery

app = Celery('tasks', broker='amqp://user:password@broker:5672')  # create celery worker server, broker is RabbitMQ


@app.task
def mul():
    # DB connection
    engine = create_engine('sqlite:///tasks.db', echo=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    # select the rows that doesn't have result
    for datarow in session.query(TaskApi.datarow).all():
        if(datarow.result is None):
            datarow.result = mul_data(datarow.rawData)  # add result to the data row
            session.add(datarow)  # update the datarow in the DB
            session.commit()  # commit all changes to DB

    session.close()


def mul_data(rawdata):  # multiplies the numbers in the raw data and returns the result
    temp_mul = 1
    lenthd = len(rawdata)
    cutarr = rawdata[1:lenthd-1]  # remove edges
    numarr = cutarr.split(',')  # split by ',' to get the numbers
    for x in numarr:
        temp_mul = temp_mul * int(x)  # multiply the numbers
    return temp_mul


