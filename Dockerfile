FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get upgrade -y

RUN apt-get install -y gdal-bin libgdal-dev
RUN apt-get install -y python3-gdal
RUN apt-get install -y binutils libproj-dev

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/