FROM python:latest

RUN apt-get update
RUN apt-get install sudo

WORKDIR /var/MPHGames

RUN sudo rm -rf RichGameiO/

RUN git clone https://github.com/igornet0/RichGameiO.git
WORKDIR /var/MPHGames/RichGameiO

RUN pip install --upgrade pip
RUN pip install mysql-connector-python
RUN pip install -r requirements.txt

CMD ["python", "main.py"]