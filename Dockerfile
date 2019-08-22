FROM python:3.7-alpine

RUN apk add -U ca-certificates 
RUN apk add --no-cache --virtual build-base gcc musl-dev libffi-dev openssl-dev make
RUN rm -rf /var/cache/apk/* 

RUN pip install --no-cache-dir --upgrade \
	pip \
	setuptools 

WORKDIR /usr/src/app/

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD run_fabric.py /usr/bin/

ENTRYPOINT ["python3", "/usr/bin/run_fabric.py"]