FROM python:3

#RUN apt-get update && apt-get -y install sudo
#RUN sudo apt-get install -y sqlite3 libsqlite3-dev
#RUN mkdir /db
#RUN /usr/bin/sqlite3 /db/test.db

RUN pip install flask==2.0.2 \
    gunicorn==20.1.0 \
    requests==2.26.0 \
    beautifulsoup4==4.10.0 \
    pytest==6.2.5

COPY . /nate_app
WORKDIR /nate_app

CMD ["/bin/bash", "run_app.sh"]