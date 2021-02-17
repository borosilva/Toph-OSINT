FROM python:3.9.1-alpine

COPY requirements.txt .

COPY . /toph

WORKDIR /toph

RUN pip install -r requirements.txt

CMD [ "python", "toph" ]