const express = require('express');
const router = express.Router();

// 임시 사용자 데이터 (DB 연동 전)
const dummyUser = {
  name: '홍길동',
  email: 'hong@example.com',
  phone: '010-1234-5678',
  created_at: '2024-01-01'
};

// 마이페이지
router.get('/', (req, res) => {
  // 로그인 체크는 나중에 세션 활용
  res.render('customer/mypage', {
    title: '마이페이지',
    user: dummyUser
  });
});

module.exports = router;