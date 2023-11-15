FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /src

COPY src/requirements.txt .

RUN pip install --upgrade pip &&  python -m pip install -r requirements.txt

COPY /src/advert ./advert
COPY /src/authentication ./authentication
COPY /src/amazon ./amazon
COPY /src/static ./static
COPY /src/user_advert_relations ./user_advert_relations
COPY /src/manage.py .