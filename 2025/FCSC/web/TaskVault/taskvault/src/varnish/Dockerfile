FROM alpine:3.21
WORKDIR /
COPY ./entrypoint.sh /entrypoint.sh
RUN apk add --update --no-cache         \
		varnish~=7.6.1-r0            && \
	chmod +x /entrypoint.sh
CMD ["/bin/sh", "/entrypoint.sh"]
