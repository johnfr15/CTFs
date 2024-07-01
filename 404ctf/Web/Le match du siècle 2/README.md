# Le match du siècle [2/2]

<br />

**Catégorie**: Web  
**Difficulté**: Moyen  
**Points**: 200  
**Connexion**: https://le-match-du-siecle.challenges.404ctf.fr

<br />
<br />

## 📃 Sommaire
- [📚 Ressources](#ressources)
- [🖼️ Introduction](#introduction)
- [🔎 Annalyse](#annalyse)
- [💡 Résolution](#résolution)
- [🚩 solution](#solution)
- [Autheur](#autheur)

<br />
<br />

## Ressources
- Burp suite: https://portswigger.net/burp/communitydownload
- Burp suite course: https://tryhackme.com/r/room/burpsuitebasics (c'est gratuit, faut juste avoir un compte)

<br/>
<br/>

## Introduction
![Le match du siècle](/img/Le%20match%20du%20siècle%20(intro).png)

<br/>
<br/>

## Annalyse

Ce challenge fait suite au premier, vous pouvez le retrouver [ici](/Web/Le%20match%20du%20siècle%201//README.md).  
comme le dit l'introduction nous devons cette fois ci obtenir des places VIP.

<br/>
<br/>

## Résolution

Tout comme le premier je décide d'utiliser **Burp suite** pour intercepter chaque requête et faire mon annalysse en profondeur des requêtes.  
Mon premier reflex ensuite a été d'essayer d'acheter un billet de la même maniere que le premier format du chall *Le match du siècle* voyant un pattern avec le nom des billets je décide de changer le nom de las requete **POST** *VIP* et d'envoyer la requête 

![Achat VIP](/img//web-1.png)

Helas cela n'a pas fonctionné et en prime je me fais bêtement repérer par le site 

![Hacker detectED](/img/hacker-detected.png)

Le poids de la culpabilité m'étant trop lourd à porter, je décide de moi-même d'aller au commissariat le plus proche pour pouvoir m'expliquer concernant mon acte d'obtenir des billets VIP gratuits. Heureusement, au milieu du chemin, je me suis rappelé que c'était dans le cadre d'un CTF donc aucun soucis enfaite.

<br/>

Une fois de retour chez moi, je continue en regardant de plus près le JWT token qui nous est donné pour essayer de faire la même manipulation, mais à partir de celui-ci, mais après quelques heures à avoir retourné ce token dans tous les sens, je passe à plusieurs énumérations.de *chemins* avec `gobuster` mais toujours rien 😭. 

<br/>

Je ne sais plus pour quelles raisons (peut-être le désespoir ? 🤔) mais en retournant dans `/billets` voir donc mes billets, je clique sur le bouton qui sert a télécharger le billet en lui même et !!!?!??

![api/riche](/img/je-suis-riche.png)

2 choses,  la première, j'apprends apparemment que je suis riche ?! C'est cool, mais ça ne m'aide pas trop à trouver le flag, si vous voyez ce que je veux dire.
Par contre, la deuxième m'intrigue, étant donné que la dernière fois c'était un POST pour acheter le billet, mais maintenant cette requête est juste pour télécharger notre billet. Ni une, ni deux, je refais la même manipulation et je change le payload `{"token": "Laterale"}` en `{"token": "VIP"}` et...  
 
<br/>

BINGO 🥳

<br/>
<br/>

## Solution 
Une requête **POST** sur l'API `/api/riche` avec comme data `{"token":"VIP"}` (même pas besoin du JWT token)   

<br/>

Avec **Burp suite**

![Burp solution](/img/le%20match%20du%20siècle%202(solution).png)

Avec curl
```bash
curl -X POST -L -o flag.png le-match-du-siecle.challenges.404ctf.fr/api/riche \
-H 'Content-Type: application/json' \
-d '{"token":"VIP"}'
```

`-X POST`: On veut envoyer une requête POST au server (par default curl envoit un requête **GET**)  
<br/>

`-L`: Ce flag va *follow* le lien si jamais on recoit une 'redirection' vers un autre endpoint (ce qui est le cas ici)  

<br/>

`-o flag.png`: le contenu téléchargé va être 'output' dans le fichier `flag.png`

<br/>

`-H 'Content-Type: application/json'`: 99% du temps avec une requête de type **POST** on veut envoyer de la data, dans ce cas avant d'inclure quelconque *payload* on est obligé de specifer ce **HEADER** `Content-Type:` (veuillez parfaitement respecter la syntax sinon ça foire). Dans notre cas on veut envoyer un *"json"* object donc lui donne en valeur `application/json`  

<br/>

`-d '{"token":"VIP"}'`: Et donc la data qui est ce *JSON* object avec comme clé/valeur `{"token":"VIP"}`

>[!TIP]
>On notera que j'ai enveloppé cette data avec *un single quote* => `'` en effet la *single quote* va nous aider à utilier la *double quote* => `"` a volonté dans ce *JSON* sans devoir mettre de `\` a chaque fois pour escape le charactere.

>[!NOTE]
>Lorsqu'il s'agit de communication ***inter-process*** il est de convention de **serialize** cette data (transformer le code en string) *code* => *string*, la donnée de sorte à ce que la data soit facilement transportable sur le reseaux.Ce format est souvent un format texte comme JSON, XML, ou un format binaire comme Protocol Buffers, MessagePack, etc. L'objectif est de rendre les données facilement transportables à travers un réseau ou entre des processus.
le sens inverse de cette opération est de **parse** la data *string* => *code*

<br/>
<br/>

## Autheur

**Tondelier Jonathan**