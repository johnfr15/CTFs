FROM alpine:3.21
WORKDIR /usr/app
COPY ./src/package.json .
RUN apk add --update --no-cache          \
        nodejs~=22                       \
        npm~=10                       && \
    npm install
COPY ./src/ .
CMD ["node", "server.js"]
