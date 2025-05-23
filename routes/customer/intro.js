// routes/intro.js
const express = require('express');
const router = express.Router();

// 인트로 페이지 렌더링
router.get('/', (req, res) => {
  res.render('customer/intro');
});

module.exports = router;