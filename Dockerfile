FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY ./requirements.txt /requirements.txt
COPY ./webserver /webserver

WORKDIR /webserver

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]

CMD [ "env FLASK_APP=server.py flask run" ]
EXPOSE 5000/tcp
