const express = require('express');
const router = express.Router();

router.get('/', (req, res) => {
  res.render('apply', {
    title: '상담 신청 | 케빈텍스'
  });
});

module.exports = router;