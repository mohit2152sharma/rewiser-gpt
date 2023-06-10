FROM python:3.10-alpine

RUN pip install -U pip
COPY . .

RUN pip install -r requirements.txt
RUN chmod +x hello.py 

ENTRYPOINT ["/main.py"]
