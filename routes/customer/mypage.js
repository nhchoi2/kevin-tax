const express = require('express');
const router = express.Router();

// 마이페이지
router.get('/', (req, res) => {
  // 세션에 사용자 정보가 없으면 로그인 페이지로 리다이렉트
  if (!req.session.user) {
    return res.redirect('/login');
  }

  // 세션의 사용자 정보 추출
  const { name, email } = req.session.user;

  // 추후 phone, created_at은 백엔드에서 추가로 받아올 수도 있음
  res.render('customer/mypage', {
    title: '마이페이지',
    user: {
      name,
      email,
      phone: '-', // 백엔드에 저장 후 확장 가능
      created_at: '-' // 추후 DB에 추가된 경우 표시
    }
  });
});

module.exports = router;