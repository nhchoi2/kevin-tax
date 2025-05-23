const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('customer/service', {
    title: '서비스 소개 - 케빈텍스'
  });
});

module.exports = router;