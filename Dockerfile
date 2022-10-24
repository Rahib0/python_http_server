FROM python:3.8

COPY . /home/ubuntu/python_server/

WORKDIR /home/ubuntu/python_server/

CMD ["python", "server.py"]