// routes/index.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('index', {
    title: '케빈텍스 | 믿을 수 있는 세무사 서비스',
    tagline: '법인·개인사업자 세무신고는 케빈텍스와 함께',
  });
});

module.exports = router;