// routes/map.js
const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('map', {
    title: '오시는 길 | 케빈텍스',
  });
});

module.exports = router;