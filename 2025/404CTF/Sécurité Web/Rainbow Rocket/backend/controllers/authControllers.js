const sqlite3 = require('sqlite3').verbose();
const jwt = require('jsonwebtoken');
const privateKey = process.env.privateKey;
const publicKey = process.env.publicKey;

let db = new sqlite3.Database('./db/users.db');

const registerUser = (req, res) => {
  const { username, password } = req.body;

  db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
    if (err) return res.status(500).json({ error: 'Internal server error' });

    if (row) {
      return res.status(401).json({ message: 'username déjà existant' });
    }

    db.run(
      'INSERT INTO users(username, password, balance) VALUES(?, ?, ?)',
      [username, password, 0],
      (err) => {
        if (err) {
          return res.status(500).json({ error: 'Internal server error' });
        }
        res.status(201).json({ message: 'User created' });
      }
    );
  });
};

const loginUser = (req, res) => {
  const { username, password } = req.body;

  db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
    if (err) return res.status(500).json({ error: 'Internal server error' });

    if (!row) {
      return res.status(401).json({ message: 'Utilisateur inexistant' });
    }

    if (row.password !== password) {
      return res.status(401).json({ message: 'Mot de passe incorrect' });
    }

    jwt.sign({ username: row.username }, privateKey, { algorithm: 'RS256' }, (err, token) => {
      if (err) return res.status(500).json({ error: 'JWT generation error' });

      res.status(200)
        .cookie('token', token, { sameSite: 'none', secure: true })
        .cookie('balance', row.balance, { sameSite: 'none', secure: true })
        .json({ username: row.username, balance: row.balance });
    });
  });
};

const verifyToken = (token) => {
  return new Promise((resolve, reject) => {
    try {
      const payload = JSON.parse(Buffer.from(token.split('.')[1], 'base64').toString());
      resolve(payload);
    } catch (err) {
      reject(new Error('Invalid token format'));
    }
  });
};

const getProfile = (req, res) => {
  const { token } = req.cookies;
  if (!token) return res.json(null);

  verifyToken(token)
    .then(user => res.json(user))
    .catch(() => res.status(401).json({ message: 'Unauthorized' }));
};

const verification = (req, res) => {
  const { token } = req.body;
  if (!token) return res.status(200).json({ message: 'Unauthorized' });

  verifyToken(token)
    .then(user => res.status(200).json({ message: user.username }))
    .catch(() => res.status(200).json({ message: 'Unauthorized' }));
};

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

module.exports = {
  registerUser,
  loginUser,
  getProfile,
  verification,
  flag
};
