FROM php:8.2-apache

RUN apt-get update && apt-get install -y apache2-bin

RUN a2enmod rewrite


COPY . /var/www/html/

RUN mkdir -p /var/files/classified && \
    echo "Mission Selenium – Niveau 5 Confidentiel\nAnalyse de l’organisme prélevé sur la face cachée lunaire : activité bioélectrique persistante.\nExpérimentations poursuivies malgré les objections éthiques.\n404CTF{fakeflag}" \
    > /var/files/classified/selenium && \
    chmod 640 /var/files/classified/selenium && \
    chown www-data:www-data /var/files/classified/selenium


RUN chmod -R 755 /var/www/html && \
    chown -R 65534:65534 /var/www/html && \
    chmod 644 /var/www/html/.htaccess || true



RUN sed -i 's/Listen 80/Listen 8080/' /etc/apache2/ports.conf && \
    sed -i 's/<VirtualHost \*:80>/<VirtualHost *:8080>/' /etc/apache2/sites-available/000-default.conf


RUN echo '<Directory "/var/">' > /etc/apache2/conf-available/restrict-var.conf && \
    echo '    Require all denied' >> /etc/apache2/conf-available/restrict-var.conf && \
    echo '</Directory>' >> /etc/apache2/conf-available/restrict-var.conf && \
    a2enconf restrict-var

    RUN echo '<Directory "/var/files/">' > /etc/apache2/conf-available/allow-var-files.conf && \
    echo '    AllowOverride All' >> /etc/apache2/conf-available/allow-var-files.conf && \
    echo '    Require all granted' >> /etc/apache2/conf-available/allow-var-files.conf && \
    echo '</Directory>' >> /etc/apache2/conf-available/allow-var-files.conf && \
    a2enconf allow-var-files

RUN echo '<Directory /var/www/html/>' >> /etc/apache2/apache2.conf && \
    echo '    AllowOverride All' >> /etc/apache2/apache2.conf && \
    echo '    Require all granted' >> /etc/apache2/apache2.conf && \
    echo '</Directory>' >> /etc/apache2/apache2.conf



EXPOSE 8080

USER www-data
