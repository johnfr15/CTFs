const User = {
  findByUsername: function(username, callback) {
    console.log(`Finding user with username: ${username}`);
    db.get('SELECT * FROM users WHERE username = ?', [username], (err, row) => {
      if (err) {
        console.log('Error finding user:', err);
      } else if (row) {
        console.log('User found:', row);
      } else {
        console.log('No user found with this username');
      }
      callback(err, row);
    });
  },

  create: function(user, callback) {
    console.log(`Creating user with username: ${user.username}`);
    db.run('INSERT INTO users (username, password, balance, billets) VALUES (?, ?, ?, ?)', 
      [user.username, user.password, user.balance, JSON.stringify(user.billets)], (err) => {
        if (err) {
          console.log('Error creating user:', err);
        } else {
          console.log('User created successfully');
        }
        callback(err);
      });
  },

  comparePassword: function(candidatePassword, hashedPassword) {
    console.log('Comparing passwords');
    return bcrypt.compare(candidatePassword, hashedPassword)
      .then(result => {
        console.log('Password comparison result:', result);
        return result;
      })
      .catch(err => {
        console.log('Error comparing passwords:', err);
        throw err;
      });
  }
};