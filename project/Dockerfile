FROM python:3.7
ENV PYTHONUNBUFFERED 1
ENV HOME_APP=/home/app
WORKDIR $HOME_APP
RUN apt-get update && apt-get install nano -y
COPY ./requirements.txt $HOME_APP
RUN pip install -r requirements.txt
COPY . $HOME_APP
