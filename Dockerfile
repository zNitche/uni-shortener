from python:3.10-slim

COPY . /uni-shortener
WORKDIR /uni-shortener

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
