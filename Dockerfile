FROM python:3.10-alpine

RUN apk update
RUN apk add git
RUN git config global -add safe.directory "*"
RUN pip install -U pip
COPY . .
ENV PYTHONUNBUFFERED=1
RUN pip install -r requirements.txt
RUN chmod +x /main.py 

ENTRYPOINT ["/main.py"]
