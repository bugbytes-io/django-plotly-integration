FROM python:3.11.2-alpine3.17

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN apk add --update --no-cache postgresql-client build-base postgresql-dev \
                                musl-dev zlib zlib-dev linux-headers

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt

COPY ./scripts /scripts
RUN chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

COPY . .
EXPOSE 80

CMD ["/scripts/run.sh"]
