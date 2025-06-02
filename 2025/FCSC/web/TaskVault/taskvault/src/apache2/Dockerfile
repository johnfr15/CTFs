FROM alpine:3.21
WORKDIR /
RUN apk add --update --no-cache                                                                        \
        apache2~=2                                                                                     \
        apache2-proxy~=2                                                                            && \
    echo "Listen 8000" >> /etc/apache2/httpd.conf 													&& \
	sed -i 's/#LoadModule proxy_module/LoadModule proxy_module/' /etc/apache2/httpd.conf 			&& \
    sed -i 's/#LoadModule proxy_http_module/LoadModule proxy_http_module/' /etc/apache2/httpd.conf  && \
    sed -i 's/ErrorLog logs\/error.log/ErrorLog \/dev\/null/g' /etc/apache2/httpd.conf              && \
    sed -i 's/    CustomLog logs/    #CustomLog logs/g' /etc/apache2/httpd.conf

COPY ./apache.conf /etc/apache2/conf.d/default.conf
CMD ["httpd", "-DFOREGROUND"]
