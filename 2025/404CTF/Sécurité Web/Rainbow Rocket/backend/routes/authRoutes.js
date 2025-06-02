const express = require('express');
const router = express.Router();
const {
  registerUser,
  loginUser,
  getProfile,
  verification,
  flag
} = require('../controllers/authControllers');

router.post('/register', registerUser);
router.post('/login', loginUser);
router.get('/profile', getProfile);
router.post('/verification', verification);
router.get('/flag', flag);

module.exports = router;
