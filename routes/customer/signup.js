const express = require('express');
const router = express.Router();

// 회원가입 페이지
router.get('/', (req, res) => {
  res.render('customer/signup', {
    title: '회원가입 | 케빈택스'
  });
});

// 회원가입 POST 처리 (DB 연결 전 임시 처리)
router.post('/', (req, res) => {
  const { name, email, password, confirmPassword, phone, agree } = req.body;
  console.log('회원가입 요청:', req.body);

  // 임시로 완료 메시지 표시 (나중에 DB 연결 시 유효성검사 및 저장 추가)
  res.send('회원가입 완료! (추후 DB 연동 예정)');
});

module.exports = router;