FROM python:3.11

EXPOSE 8000

COPY requirements.txt /requirements.txt
RUN python3 -m pip install -r /requirements.txt

COPY . /info-stambul-ui

CMD cd /info-stambul-ui && python3 manage.py runserver
