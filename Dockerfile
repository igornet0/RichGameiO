FROM python:latest

RUN pip install --upgrade pip
RUN pip install mysql-connector-python

WORKDIR /var/MPHGames
RUN cd /var/MPHGames

RUN apt-get update
RUN apt-get install sudo

RUN sudo rm -rf RichGameiO/

RUN git clone https://github.com/igornet0/RichGameiO.git

RUN pip install -r RichGameiO/requirement.txt

RUN python RichGameiO/main.py