FROM python:3.11.3-alpine3.16

COPY requirements.txt /requirements.txt
COPY src /src

WORKDIR /src
EXPOSE 8000

RUN apk add postgresql-client build-base postgresql-dev
RUN pip install -r ../requirements.txt

RUN addgroup -S projectuser
RUN adduser --disabled-password -S projectuser -G projectuser

RUN chown -R projectuser:projectuser /src
RUN chmod 666 -R /usr/local/lib/python3.11/site-packages/rest_framework_jwt/blacklist/migrations
USER projectuser