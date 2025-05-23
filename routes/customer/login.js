const express = require('express');
const router = express.Router();

// 임시 사용자 데이터 (DB 연동 전용 Mock)
const dummyUser = {
  email: 'user@example.com',
  password: '1234'
};

router.get('/', (req, res) => {
  res.render('customer/login', { title: '로그인' });
});

router.post('/customer/login', (req, res) => {
  const { email, password } = req.body;

  if (email === dummyUser.email && password === dummyUser.password) {
    req.session.user = email;
    return res.redirect('/customer/mypage'); // 로그인 성공 시 마이페이지 이동
  }

  res.send('<script>alert("이메일 또는 비밀번호가 틀렸습니다."); location.href="/customer/login";</script>');
});

module.exports = router;