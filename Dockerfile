FROM python:latest

RUN pip install mysql-connector-python

WORKDIR /var/MPHGames
RUN cd /var/MPHGames

RUN git clone https://github.com/igornet0/RichGameiO.git
RUN cd RichGameiO

RUN python main.py