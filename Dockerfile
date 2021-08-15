FROM python:3.8

COPY requirements.txt /tmp/

RUN apt-get update
RUN apt -qq -y install python-opencv
RUN pip install -r /tmp/requirements.txt

COPY src/ /

CMD ["python3", "/main.py", "--src", "/DATA/"]
