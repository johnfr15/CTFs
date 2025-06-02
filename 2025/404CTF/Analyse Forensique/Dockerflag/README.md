![intro](/img/intro.png)


<br>
<br>

## Ressources utiles:

- **Quelque commandes docker sympa**: https://docs.docker.com/reference/cli/docker/image/ 
- **Comment git fonctionne**: https://git-scm.com/book/en/v2/Git-Internals-Git-References 

<br>
<br>

on nous donne le `.tar` d'une image docker, qu'on peut de suite load avec la commande
```bash
docker load < dockerflag.tar
```

<br>

Nous donnant l'image suivante
```bash
unset-repo/unset-image-name                latest        3f2e4c8bd571   2 months ago    166MB
```

<br>

ma première idée était de faire un `docker inspect` de cette image pour y voir toute ses métadonnées
```bash
docker inspect 3f2e4c8bd571 | jq
[
  {
    "Id": "sha256:3f2e4c8bd571c28bbc2d539723b528a35483cfed20d8db833f8dd14bc04363ec",
    "RepoTags": [
      "unset-repo/unset-image-name:latest"
    ],
    "RepoDigests": [],
    "Parent": "",
    "Comment": "",
    "Created": "2025-03-03T17:17:58.105682612Z",
    "DockerVersion": "",
    "Author": "",
    "Config": {
      "Hostname": "",
      "Domainname": "",
      "User": "",
      "AttachStdin": false,
      "AttachStdout": false,
      "AttachStderr": false,
      "Tty": false,
      "OpenStdin": false,
      "StdinOnce": false,
      "Env": [
        "PATH=/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin",
        "LANG=C.UTF-8",
        "GPG_KEY=A035C8C19219BA821ECEA86B64E628F8D684696D",
        "PYTHON_VERSION=3.11.11",
        "PYTHON_SHA256=2a9920c7a0cd236de33644ed980a13cbbc21058bfdc528febb6081575ed73be3"
      ],
      "Cmd": [
        "python3",
        "app.py"
      ],
      "Image": "",
      "Volumes": null,
      "WorkingDir": "/app",
      "Entrypoint": null,
      "OnBuild": null,
      "Labels": null
    },
    "Architecture": "amd64",
    "Os": "linux",
    "Size": 165914752,
    "GraphDriver": {
      "Data": {
        "LowerDir": "/var/lib/docker/overlay2/ce286d654f3b80280dda2f5aeb3fe9bf6d4ca1fa88337173b30edd15692c46ac/diff:/var/lib/docker/overlay2/89586374ff38a5239b67a7a513ada8095e77733929778b0e849813e42c64e32b/diff:/var/lib/docker/overlay2/caa6b8ecfadf9619e0463b1d88d1fdc01e43c94f4b493b17811a0aa911a7564b/diff:/var/lib/docker/overlay2/866bf0278c7bdb79a8f0b25653947bedf28d5bf69fbfda90d7e95b59cf187b97/diff:/var/lib/docker/overlay2/48a60fa0246948644b532b2d4c6601a7294371644d5a1914334054ad7c08d19d/diff:/var/lib/docker/overlay2/ae9a0e2f8d3ce6d22d613628b4ed40b0316137d78b9b9de138a59803cdb718ac/diff:/var/lib/docker/overlay2/61eff6c1548bfea4475fa84da50ac19eb50cd493fd3c85d0dcc63c604b098f84/diff:/var/lib/docker/overlay2/584794ae3492b4fad731cc16558b96da7e20c721948e671d1bde6943df27dc2d/diff",
        "MergedDir": "/var/lib/docker/overlay2/71b984c14e7577a7904e4fc9feb0a31e5dc1d8d0515222e8262092fe4d1bfc20/merged",
        "UpperDir": "/var/lib/docker/overlay2/71b984c14e7577a7904e4fc9feb0a31e5dc1d8d0515222e8262092fe4d1bfc20/diff",
        "WorkDir": "/var/lib/docker/overlay2/71b984c14e7577a7904e4fc9feb0a31e5dc1d8d0515222e8262092fe4d1bfc20/work"
      },
      "Name": "overlay2"
    },
    "RootFS": {
      "Type": "layers",
      "Layers": [
        "sha256:5f1ee22ffb5e68686db3dcb6584eb1c73b5570615b0f14fabb070b96117e351d",
        "sha256:02e5dc3ed962b7d6c5a61ff01528a8760125f47b531bc2999d6d3990d67bd01a",
        "sha256:1482d10861f734911f5dac47d8647096396e41d99de1804110f318836b5a4283",
        "sha256:7dc6e24448644a289443a056c738aa42ba357ed08e249e9db879e35a869b3697",
        "sha256:1f4e3e92956bc82a56972ddeaac358246284b4ce298c430dbdd9e2f287bae0e7",
        "sha256:18db75dd3ab7f29d5df13a3c1b1639aa00fc25bfa8be7a071d2f72e78aea4796",
        "sha256:3b36af5ed5aa2e17ad02c5d2b0cb9c670ed4a7163c4e779955be4a1eed5826c7",
        "sha256:9f340e8f2de8fef5b8971a1659c529d18cc40a7af9c1140df24012a660ac6370",
        "sha256:00370dc2b679c5a7dc18eb94cb8d6dd6182390db7fc4161d83fb5400bb55ee00"
      ]
    },
    "Metadata": {
      "LastTagTime": "0001-01-01T00:00:00Z"
    }
  }
]
```

notamment les ENVs qui y sont données lors de l'execution du container, mais rien de juteux 

<br>

J'execute donc le containeur, peut-être que je trouverais de la data pertinent dedans directement.
```bash
docker run -it unset-repo/unset-image-name:latest bash
```

avec une commande du style `find / -type f | grep 404CTF` ou depuis l'app en faisant une commande `strings` sur tout les fichiers 
```bash
find /app -type f -exec cat {} >> out.txt \; 
strings out.txt | grep 404
```

mais là non plu rien de concluant.
(By the way j'ai du download la commande `strings` parcequ'elle existe pas nativement dans l'image => `apt install binutils`)

<br>

Ducoup cette fois je vais essayer de voir quelles ont été les commandes docker lors de la construction des layers pour y voir plus clair

```bash
docker history unset-repo/unset-image-name:latest 

IMAGE          CREATED        CREATED BY                                      SIZE      COMMENT
3f2e4c8bd571   N/A            RUN rm -rf .git                                 0B        
<missing>      N/A            RUN pip install -r requirements.txt             16.5MB    
<missing>      N/A            RUN apt update && apt upgrade -y                19.6MB    
<missing>      N/A            COPY git_repos/ .                               23.5kB    
<missing>      N/A            WORKDIR /app                                    0B        
<missing>      5 months ago   CMD ["python3"]                                 0B        buildkit.dockerfile.v0
<missing>      5 months ago   RUN /bin/sh -c set -eux;  for src in idle3 p…   36B       buildkit.dockerfile.v0
<missing>      5 months ago   RUN /bin/sh -c set -eux;   savedAptMark="$(a…   45.8MB    buildkit.dockerfile.v0
<missing>      5 months ago   ENV PYTHON_SHA256=2a9920c7a0cd236de33644ed98…   0B        buildkit.dockerfile.v0
<missing>      5 months ago   ENV PYTHON_VERSION=3.11.11                      0B        buildkit.dockerfile.v0
<missing>      5 months ago   ENV GPG_KEY=A035C8C19219BA821ECEA86B64E628F8…   0B        buildkit.dockerfile.v0
<missing>      5 months ago   RUN /bin/sh -c set -eux;  apt-get update;  a…   9.24MB    buildkit.dockerfile.v0
<missing>      5 months ago   ENV LANG=C.UTF-8                                0B        buildkit.dockerfile.v0
<missing>      5 months ago   ENV PATH=/usr/local/bin:/usr/local/sbin:/usr…   0B        buildkit.dockerfile.v0
<missing>      5 months ago   # debian.sh --arch 'amd64' out/ 'bookworm' '…   74.8MB    debuerreotype 0.15
```

hmm cela semble intéressant, on voit que la tout dernière commande éxecuté est `RUN rm -rf .git ` el famoso `.git` qui est source de plein de data intéressante !
on voit aussi le layer qui l'a introduit `COPY git_repos/ .`

ducoup lets go récuperer chaque layers de la ressource original (j'ai pris soin de mettre cela dans un directory à part [dockerflag](/dockerflag/))

```bash
tar -xvf resources/dockerflag.tar -C dockerflag
```

Nous voilà donc avec => 
```bash
➜  dockerflag ll
total 68M
-rw-r--r-- 1 john john  250 Jan  1  1970 0c5ce2cb4ecc4aadbe1ed2f03df63b0a280a041c1b61fe1cde8d9af1ee5de163.tar.gz
-rw-r--r-- 1 john john 3.4M Jan  1  1970 183f0922284a8cedfbb884126f80363579bb8dbca1911951bfd7f0ee1d710f11.tar.gz
-rw-r--r-- 1 john john 7.1M Jan  1  1970 2dd9efc95e3bde1e4ef8e0fcd71ec913569877acacea9c1cf149a6fa3c4f1e15.tar.gz
-rw-r--r-- 1 john john  16M Jan  1  1970 5dbb3b698b727bb06ce21e20ef60f7929e05ea0746047bb970d01e34ee6129ad.tar.gz
-rw-r--r-- 1 john john  235 Jan  1  1970 5e76ef2b84193ccb29c672d49c9f9134aaac6c2f9af4f26b44584d5190f3dc41.tar.gz
-rw-r--r-- 1 john john  27M Jan  1  1970 7cf63256a31a4cc44f6defe8e1af95363aee5fa75f30a248d95cae684f87c53c.tar.gz
-rw-r--r-- 1 john john  25K Jan  1  1970 c0f44320de6915ebd75512f6564344e5aac1b91cb82573690a8061f561804aad.tar.gz
-rw-r--r-- 1 john john  298 Jan  1  1970 c3e571d9ad58726bad8935e6692b4f21152237c4fdd0a1c913101361cc091fb7.tar.gz
-rw-r--r-- 1 john john  15M Jan  1  1970 d0348a7011341bc6ddc97a59c8ad3a07c2b31b179030dec19460f12a463e3420.tar.gz
-rw-r--r-- 1 john john  917 May 22 09:08 manifest.json
-rw-r--r-- 1 john john 6.1K Jan  1  1970 sha256:3f2e4c8bd571c28bbc2d539723b528a35483cfed20d8db833f8dd14bc04363ec
```

Tout les layers de l'image.

C'est là que ça devient un peu technique on va devoir se focus que sur les layers concernés depuis le *COPY* jusqu'au *RUN rm* inutile de se concentrer sur les autres layers pour le moment.

donc...

Comment savoir quelles layers appartient à quelle command de notre `docker history` précédemment ? C'est la que le [`manifest.json`](https://docs.docker.com/reference/cli/docker/manifest/) présent dans le tarball fait tout son sens, on y voit tout less layers ordonnées

```bash
cat manifest.json | jq
[
  {
    "Config": "sha256:3f2e4c8bd571c28bbc2d539723b528a35483cfed20d8db833f8dd14bc04363ec",
    "RepoTags": ["docker.io/unset-repo/unset-image-name:latest"],
    "Layers": [
      "7cf63256a31a4cc44f6defe8e1af95363aee5fa75f30a248d95cae684f87c53c.tar.gz",
      "183f0922284a8cedfbb884126f80363579bb8dbca1911951bfd7f0ee1d710f11.tar.gz",
      "5dbb3b698b727bb06ce21e20ef60f7929e05ea0746047bb970d01e34ee6129ad.tar.gz",
      "0c5ce2cb4ecc4aadbe1ed2f03df63b0a280a041c1b61fe1cde8d9af1ee5de163.tar.gz",
      "5e76ef2b84193ccb29c672d49c9f9134aaac6c2f9af4f26b44584d5190f3dc41.tar.gz",
      "c0f44320de6915ebd75512f6564344e5aac1b91cb82573690a8061f561804aad.tar.gz",
      "d0348a7011341bc6ddc97a59c8ad3a07c2b31b179030dec19460f12a463e3420.tar.gz",
      "2dd9efc95e3bde1e4ef8e0fcd71ec913569877acacea9c1cf149a6fa3c4f1e15.tar.gz",
      "c3e571d9ad58726bad8935e6692b4f21152237c4fdd0a1c913101361cc091fb7.tar.gz"
    ]
  }
]
```
Le `layers[0]` étant la base, nous allons nous concentrer sur les quatre derniers qui nous intéressent. 

ni une ni deux je me fait un petit setup propre

```bash
cd dockerflag
mkdir layers
mkdir layers/layer{0..9}
tar -zxvf c3e571d9ad58726bad8935e6692b4f21152237c4fdd0a1c913101361cc091fb7.tar.gz -C ./layers/layer9
tar -zxvf 2dd9efc95e3bde1e4ef8e0fcd71ec913569877acacea9c1cf149a6fa3c4f1e15.tar.gz -C ./layers/layer8
tar -zxvf d0348a7011341bc6ddc97a59c8ad3a07c2b31b179030dec19460f12a463e3420.tar.gz -C ./layers/layer7
tar -zxvf c0f44320de6915ebd75512f6564344e5aac1b91cb82573690a8061f561804aad.tar.gz  -C ./layers/layer6
```

Ok normalement si on est des snipers, le .git devrait se trouver pour la toute première fois danss le layer6

```bash
cd layers/layer6
ls
app
cd app/
ls -la
total 28
drwxr-xr-x 5 john john 4096 Mar  3 18:17 .
drwxr-xr-x 3 john john 4096 Mar  3 18:17 ..
-rw-r--r-- 1 john john  305 Mar  3 18:17 app.py
drwxr-xr-x 5 john john 4096 May 22 09:17 .git
-rw-r--r-- 1 john john  130 Mar  3 18:17 requirements.txt
drwxr-xr-x 2 john john 4096 Mar  3 18:17 static
drwxr-xr-x 2 john john 4096 Mar  3 18:17 templates
```

Bingo \**sun glass emoji*\*

reste plus qu'a s'amuser avec ! 

```bash
git log
fatal: not a git repository (or any of the parent directories): .git
```

Uh uh ? Masaka !!

on dirait que le git est endomagé regardons cela avec la commande `tree`

```bash
tree .git
.git
├── logs
│   ├── HEAD
│   └── refs
│       └── heads
│           └── main
├── objects
│   ├── 05
│   │   └── 34ef13bca01be8d3799ae71b71390f3da6a137
│   ├── 1c
│   │   └── d55b1dad90de7013822452467b23374adf1d96
│   ├── 2c
│   │   └── e2d47d98a2619eb78554fef2715d963292a3a8
│   ├── 35
│   │   └── 0f10b0c9123e09b88ef2a05fd76848902fd677
│   ├── 3d
│   │   └── 0717cb911d00b3e5033ba8c0c83df069e3e144
│   ├── 3e
│   │   └── 384b4f7e3d7b85a8fe59c07f79f0a1d04919a1
│   ├── 4b
│   │   └── 825dc642cb6eb9a060e54bf8d69288fbee4904
│   ├── 51
│   │   └── 4443de0db750428f03d41d2be47e8c6d066981
│   ├── 55
│   │   └── 86fa52c83891ac0489f6f17b6bae9236bbccd0
│   ├── 7b
│   │   └── 3d21bc77b2acda6d6c4c94f51a4bb01d6504f8
│   ├── 82
│   │   └── 2a5257be1ed6d883e84877f7ba2253b294fa96
│   ├── b3
│   │   └── 4c648f6790f6dee4340767ddf4b077f639132d
│   ├── c8
│   │   └── e66485c89a29768dd546a3046b8544520615d6
│   ├── db
│   │   └── e4f9e3a6014eaf1e13f07660284fc5465a3cb4
│   ├── e3
│   │   └── a5491ad536b35974022c3b521d3b48880afb68
│   ├── e6
│   │   └── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│   ├── e8
│   │   └── deb9b0d6324225d8b728dece8b2de908abcd81
│   ├── eb
│   │   └── 633388d340c6d9613fe7d48e8e4b56ec4460d7
│   ├── fc
│   │   └── 29f474601267e99d2e9e5861e978fb33de36c9
│   ├── info
│   └── pack
└── refs
    ├── heads
    │   └── main
    └── tags

29 directories, 22 files
```

Bon la c'est le moment où il faut connaitre .git et son fonctionnement ducoup laissons chatGPT nous expliquer

[!NOTE]
> ***explique moi chaque élèment de se .git et pourquoi cela ne marche pas ?***
> REPONSE: https://chatgpt.com/share/682ee5a4-6834-8011-b395-5b176722bdd3

Ok il manque just le fichier `HEAD` avec les bonnes informations pour qu'il puisse pointer sur la branch `main`
soit:

```bash
echo "ref: refs/heads/main" > .git/HEAD
```

et hop !
```bash
git log
commit e3a5491ad536b35974022c3b521d3b48880afb68 (HEAD -> main)
Author: Alba Laine <stagiare@docker.flag>
Date:   Mon Mar 3 17:17:28 2025 +0000

    Add HTML website

commit b34c648f6790f6dee4340767ddf4b077f639132d
Author: Alba Laine <stagiare@docker.flag>
Date:   Mon Mar 3 17:17:28 2025 +0000

    Requirements of website

commit 514443de0db750428f03d41d2be47e8c6d066981
Author: Alba Laine <stagiare@docker.flag>
Date:   Mon Mar 3 17:17:28 2025 +0000

    Add static ressources

commit 3d0717cb911d00b3e5033ba8c0c83df069e3e144
Author: Alba Laine <stagiare@docker.flag>
Date:   Mon Mar 3 17:17:28 2025 +0000

    Last commit before week-end !
:
```
Reste plus qu'a voir tout les détailles des commits.
Quand on regarde les messages on voit que le stagiaRE fait un commit juste avant le weekend, donc en générale fin de week source de fatigue tous sa tous sa

en vrai just un `git diff` fait parfaitement l'affaire entre ce commit et le dernier

```bash
git diff c8e66485c89a29768dd546a3046b8544520615d6 e3a5491ad536b35974022c3b521d3b48880afb68

diff --git a/.env b/.env
deleted file mode 100644
index 350f10b..0000000
--- a/.env
+++ /dev/null
@@ -1 +0,0 @@
-SECRET="404CTF{492f3f38d6b5d3ca859514e250e25ba65935bcdd9f4f40c124b773fe536fee7d}"
diff --git a/requirements.txt b/requirements.txt
new file mode 100644
index 0000000..5586fa5
--- /dev/null
+++ b/requirements.txt
@@ -0,0 +1,8 @@
+blinker==1.9.0
+click==8.1.8
+Flask==3.1.0
+itsdangerous==2.2.0
+Jinja2==3.1.5
+MarkupSafe==3.0.2
+python-dotenv==1.0.1
+Werkzeug==3.1.3
diff --git a/static/logo.png b/static/logo.png
new file mode 100644
...
```

Le flag apparait ! (en vrai j'ai eu de la chance parceque faire un diff entre le tout premier commit et le dernier, on l'aurait pas vu)

Une autre manière un peu plus "brut" aurait été de check chaque BLOB dans `.git/objects`. Etant donnée que ces fichiers sont `zlib`, c'est la raison pour laquelle on n'a vu avec notre command `strings` du début. 

Donc pour `objects/05/34ef13bca01be8d3799ae71b71390f3da6a137`, on éxecutera

```bash
git cat-file -p 0534ef13bca01be8d3799ae71b71390f3da6a137                                  

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <link rel="stylesheet" href="static/style.css">
    <title>Dockerflag</title>
  </head>
  <body>
    <nav class="navbar navbar-expand-lg navbar-dark bg-info">
  <a class="navbar-brand" href="#">
    Dockerflag
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarSupportedContent">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#">About</a>
      </li>
    </ul>
    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search for the flag" aria-label="Search">
      <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Get the flag</button>
    </form>
  </div>
</nav>
<section class="vh-100" style="background-color: #eee;">
  <div class="container py-5 h-100">
    <div class="row d-flex justify-content-center align-items-center h-100">
      <div class="col col-lg-9 col-xl-7">
        <div class="card" style="border-radius: 15px;">
          <div class="card-body p-5">

            <div class="text-center mb-4 pb-2">
              <img src="/static/logo.png"
                alt="Bulb" width="100">
            </div>

            <figure class="text-center mb-0">
              <blockquote class="blockquote">
                <p class="pb-3">
                  <i class="fas fa-quote-left fa-xs text-primary"></i>
                  <span class="lead font-italic">Dockerflag : un docker, un flag</span>
                  <i class="fas fa-quote-right fa-xs text-primary"></i>
                </p>
              </blockquote>
              <figcaption class="blockquote-footer mb-0">
                Alba Leine
              </figcaption>
            </figure>

          </div>
        </div>
      </div>
    </div>
  </div>
</section>

  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/popper.js@1.14.7/dist/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.3.1/dist/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
  </body>
</html>%                                                                                                                
```

<br>

et hop on voit l'objets tel quel, et on note là, la subtilité de git de se servir du hash comme sous répertoire pour stocker ses objets lié

dans ce try hard de blob display le flag se trouvait dans l'objets `.git/objects/35/0f10b0c9123e09b88ef2a05fd76848902fd677`

## Auteur
Tondelier Jonathan