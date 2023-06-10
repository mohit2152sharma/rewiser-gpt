FROM python:3.10-alpine

RUN pip install -U pip
WORKDIR /app 
COPY . /app 

RUN pip install -r requirements.txt
RUN chmod +x /app/main.py 

ENTRYPOINT ["/app/main.py"]
