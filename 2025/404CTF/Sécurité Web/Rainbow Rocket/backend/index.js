const express = require('express');
const dotenv = require('dotenv').config();
const cors = require('cors');
const sqlite3 = require('sqlite3').verbose();
const cookieParser = require('cookie-parser');
const logger = require('./logger'); // Optional logging
const authRoutes = require('./routes/authRoutes');

const app = express();
const port = 8000;

// Middleware
app.use(cors({
  origin: process.env.FRONTEND_URL,
  credentials: true,
  methods: 'GET,POST,PUT,DELETE',
  allowedHeaders: 'Content-Type,Authorization'
}));
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use('/api', authRoutes);

// DB Setup
let db = new sqlite3.Database('./db/users.db', (err) => {
  if (err) {
    logger.error(`Error connecting to SQLite: ${err.message}`);
  } else {
    console.log('DB connected');
    db.run(`
      CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        balance INTEGER DEFAULT 0
      )
    `, (err) => {
      if (err) {
        logger.error(`Error creating table: ${err.message}`);
      } else {
        console.log('Users table ready');
      }
    });
  }
});

// Error Handling
process.on('unhandledRejection', (error) => {
  logger.error(`Unhandled Rejection: ${error.message}`);
});

process.on('uncaughtException', (error) => {
  logger.error(`Uncaught Exception: ${error.message}`);
});

// Start Server
app.listen(port, () => {
  console.log(`Server running on port ${port}`);
});
