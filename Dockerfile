# FROM alpine:latest
# COPY . .
# RUN apk add --update \
#     python \
#     python-dev \
#     py-pip \
#     build-base \
#   && pip install virtualenv \
#   && rm -rf /var/cache/apk/*

# WORKDIR /app

# ONBUILD COPY . /app
# ONBUILD RUN virtualenv /env && /env/bin/pip install -r /app/requirements.txt

# EXPOSE 8080
# #CMD ["/env/bin/python", "main.py"]

FROM python:3.7-alpine

COPY requirements.txt /
RUN pip install -r /requirements.txt

COPY . /app
WORKDIR /app

CMD ["python", "/app/secret_util.py"]
