const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('customer/settings', {
    title: '설정 | 케빈텍스'
  });
});

module.exports = router;