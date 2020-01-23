FROM python:3.7.3-alpine

COPY ./app.py /opt/app/app.py
COPY ./requirements.txt /opt/app/requirements.txt
WORKDIR /opt/app

RUN pip install -r ./requirements.txt
EXPOSE 8000

CMD ["python", "./app.py"]
