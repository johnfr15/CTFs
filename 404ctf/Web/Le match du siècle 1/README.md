# Le match du siècle [1/2]

<br />

**Catégorie**: Web  
**Difficulté**: Introduction  
**Points**: 200  
**Connexion**: https://le-match-du-siecle.challenges.404ctf.fr

<br />
<br />

## 📃 Sommaire
- [📚 Ressources](#ressources)
- [🖼️ Introduction](#introduction)
- [🔎 Annalyse](#annalyse)
- [💡 Résolution](#solution)
- [💭 Conclusion](#conclusion)
- [Autheur](#autheur)

<br />
<br />

## Ressources
- Burp suite: https://portswigger.net/burp/communitydownload
- Burp suite course: https://tryhackme.com/r/room/burpsuitebasics (c'est gratuit, faut juste avoir un compte)

<br/>
<br/>

## Introduction
![Le match du siècle](/img/Le%20match%20du%20siècle%201%20(intro).png)

<br/>
<br/>

## Annalyse

Il suffit simplement de se procurer un billet EZ. En arrivant sur le site on peut s'incrire mais à partir de là à nous de trouver.

<br/>
<br/>

## Résolution

>[!NOTE]
> *Fun fact avant de faire l'inscription j'avais essayé de me connecter au site avec le scrédentials Admin123/Admin123 et apparement quelqu'un d'autre (qui avait déjà pwn ce chall) a eu la même idée que moi, ducoup je suis passé derrière récup le flag sans rien faire*

*First thing first* j'ouvre **Burp suite** pour intercepter chaque requête et faire mon annalysse en profondeur des requêtes.  
Mon premier reflex ensuite a été d'essayer d'acheter un billet **Lateral** directement depuis le site 

![Achat Lateral](/img/achat-billet-lateral.png)

Helas comme cela spécifier dans la requête avant l'envoie ma *balance* est a `0` impossible d'acheter de cette façon

![Hacker detectED](/img/solde-insufficient.png)

<br/>

Ducoup tout simplement je décide de refaire la même requete mais de simuler une balance a `40`(le prix du billet) et...

BINGO 🥳  
  
Il suffit ensuite de télécharger le flag PNG de puis notre billet recemment acheté depuis ce endpoint `/billets`.

<br/>
<br/>

## Solution 
Dans les cookies il suffit juste de changer la valeur du champ `balance` avec le prix du billet (ou) plus  

<br/>

### Butp Suite

    Avec Burp suite

![Burp solution](/img/Le%20match%20du%20siècle%201%20(solution).png)

<br/>
<br/>

### Curl

    Avec curl

Premièrement pour réussir cette achat il nous faut récuper notre 'token' d'authentifaction (JWT token) token qu'on va stocker dans notre variable d'environnement 'JWT'

***Methode 1***
Utilisez l'option -c pour spécifier un fichier de cookies:

```bash
curl -X POST le-match-du-siecle.challenges.404ctf.fr/api/login \
-H 'Content-Type: application/json' \
-d '{"username":"your_username", "password":"your_password"}' \
-c cookie.txt
```

***Methode 2***
Utilisez l'option -i pour inclure les en-têtes de réponse dans la sortie curl :

```bash
curl -X POST le-match-du-siecle.challenges.404ctf.fr/api/login \
-H 'Content-Type: application/json' \
-d '{"username":"your_username", "password":"your_password"}' \
-i 
```

<br/>

***Utilisation de curl pour récupérer un JWT***

J'ai personnellement choisi la ***method 2***. Evidemment seulement le **JWT token** m'interesse, ce qui nous fait au final 

```bash
JWT=$(curl -X POST -L le-match-du-siecle.challenges.404ctf.fr/api/login \
-H 'Content-Type: application/json' \
-d '{"username":"your_username", "password":"your_password"}' \
-i | grep "set-cookie: token=" | cut -d ' ' -f2 | awk -F 'token=|;' '{print $2}')
```

Pas mal de chose dans cette commande, regardons étape par étape

- `JWT=$(...)`: Cette syntaxe permet de stocker la sortie de la commande dans la variable JWT.

- `curl -X POST -L le-match-du-siecle.challenges.404ctf.fr/api/login:`

    - `-X POST`: On veut envoyer une requête POST au serveur (par défaut, curl envoie une requête GET).
    - `-L`: Ce flag permet de suivre la redirection si jamais on reçoit une réponse de redirection vers un autre endpoint (ce qui est souvent le cas lors des connexions).
    - `-H 'Content-Type: application/json'`: Ce header indique que le type de contenu envoyé au serveur est du JSON.
    - `-d '{"username":"your_username", "password":"your_password"}'`: Les données envoyées dans le corps de la requête. Ici, il s'agit d'un objet JSON contenant les identifiants de connexion.
    - `-i`: Inclut les en-têtes HTTP dans la sortie.

<br/>

>[!TIP]
>On notera que j'ai enveloppé cette data avec *un single quote* => `'` en effet la *single quote* va nous aider à utilier la *double quote* => `"` a volonté dans ce *JSON* sans devoir mettre de `\` a chaque fois pour escape le charactere.

<br/>

**Traitement de la sortie avec grep, cut et awk**

- `| grep "set-cookie: token="`: Filtre la sortie de curl pour ne garder que les lignes contenant `set-cookie: token=`, car c'est là où le JWT est envoyé par le serveur.

- `| cut -d ' ' -f2`: Sépare la ligne par des espaces (-d ' ') et récupère le deuxième champ (-f2), qui est la partie contenant le token= et le reste de l'en-tête.

- `| awk -F 'token=|;' '{print $2}'`:

    - `-F 'token=|;'`: Spécifie plusieurs séparateurs de champ, `token=` et `;`.
    - `{print $2}`: Affiche le deuxième champ, qui est le JWT proprement dit.

<br/>

***Utilisation de curl pour acheter le billet***

Un petit `echo $JWT` pour s'assurer que tout est bien en place et une fois notre token `JWT` récuperé, on va pouvoir passer a la commande suivante et bypass notre `balance`

```bash
curl -X POST -L le-match-du-siecle.challenges.404ctf.fr/api/achat \
-b "balance=40; token=$JWT" \
-H 'Content-Type: application/json' \
-d '{"numero":"Laterale"}'
```
- `-X POST`: Indique que la requête à envoyer est de type POST.
- `-L`: Permet de suivre les redirections si elles sont présentes.
- `-b "balance=40; token=$JWT"`: Envoie les cookies dans la requête. Ici, on inclut à la fois la balance et le token JWT. Le token JWT est récupéré de la variable JWT grâce à $JWT.
- `-H 'Content-Type: application/json'`: Indique que le type de contenu envoyé au serveur est du JSON.
- `-d '{"numero":"Laterale"}'`: Les données envoyées dans le corps de la requête. Ici, il s'agit d'un objet JSON contenant le numéro du billet que vous souhaitez acheter ("Laterale", on se met bien hehe).


>[!NOTE]
>Lorsqu'il s'agit de communication ***inter-process*** il est de convention de **serialize** cette data (transformer le code en string) *code* => *string*, la donnée de sorte à ce que la data soit facilement transportable sur le reseaux.Ce format est souvent un format texte comme JSON, XML, ou un format binaire comme Protocol Buffers, MessagePack, etc. L'objectif est de rendre les données facilement transportables à travers un réseau ou entre des processus.
le sens inverse de cette opération est de **parse** la data *string* => *code*


***Récuperation du flag***

Avec notre nouveau billet acheté (lol) on va pouvoir voir quelle est le **endpoint** pour pouvoir télécharger le *billet*(flag) 

```bash
curl -X POST -L -o flag.png le-match-du-siecle.challenges.404ctf.fr/api/riche \
-H 'Content-Type: application/json' \
-d '{"token":"laterale"}'
```

- `-X POST`: Indique que la requête à envoyer est de type POST.
- `-L`: Permet de suivre les redirections si elles sont présentes.  
- `-o flag.png`: le contenu téléchargé va être 'output' dans le fichier `flag.png`
- `-H 'Content-Type: application/json'`: 99% du temps avec une requête de type **POST** on veut envoyer de la data, dans ce cas avant d'inclure quelconque *payload* on est obligé de specifer ce **HEADER** `Content-Type:` (veuillez parfaitement respecter la syntax sinon ça foire). Dans notre cas on veut envoyer un *"json"* object donc lui donne en valeur `application/json`  
- `-d '{"token":"Laterale"}'`: Et donc la data qui est ce *JSON* object avec comme clé/valeur `{"token":"Laterale"}`

<br/>
<br/>

## Conclusion
Conclusion bien que la notre vrai balance est été spécifié dans le JWT token il semblerait que la back end reagrde seulement celui dans nos cookie, la difference c'est que n'importe quelle valeur peut être arbitrairement changé par le client contrairement aux JWT où sa dernière parti est *signé* par la une clé privée par le backend rendant donc toute modification repèrable facilement.

<br/>
<br/>

## Autheur

**Tondelier Jonathan**