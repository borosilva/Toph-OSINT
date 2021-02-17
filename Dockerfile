FROM python:3.9.1-alpine

COPY requirements.txt .

COPY . /toph

WORKDIR /toph

CMD [ "python", "toph" ]