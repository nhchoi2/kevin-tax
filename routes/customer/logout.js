// routes/customer/logout.js
const express = require('express');
const router = express.Router();

// 로그아웃 → 세션 삭제 후 홈으로 이동
router.get('/', (req, res) => {
  req.session.destroy(() => {
    res.redirect('/');
  });
});

module.exports = router;