from python:3.10-slim

COPY . /uni_shortener
WORKDIR /uni_shortener

RUN pip3 install -r requirements.txt

ENTRYPOINT ["sh", "entrypoint.sh"]
