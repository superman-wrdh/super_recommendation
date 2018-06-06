FROM docker.io/python:3.5
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY . /usr/src/app
RUN pip install -r /usr/src/app/requirements.txt -i https://pypi.douban.com/simple/


