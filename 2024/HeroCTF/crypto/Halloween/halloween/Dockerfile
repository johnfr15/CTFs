FROM python:3.11-alpine

RUN apk --no-cache add socat \
    && adduser -D --home /app user \
    && pip3 install --no-cache-dir gostcrypto flask

RUN echo 'FLAG{yolo}' > /flag.txt

COPY --chown=user . /app

WORKDIR /app

# Set a default port if LISTEN_PORT is not provided
ENV LISTEN_PORT=8000
EXPOSE ${LISTEN_PORT}

ENTRYPOINT ["python3 /app/chall2.py"]
