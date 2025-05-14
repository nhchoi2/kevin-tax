// routes/blog.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('blog', {
    title: '케빈텍스 블로그',
  });
});

module.exports = router;