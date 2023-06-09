FROM python:3.10-alpine

RUN pip install -u pip
COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["hello.py"]
