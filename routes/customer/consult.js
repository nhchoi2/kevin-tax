const express = require('express');
const router = express.Router();

// 임시 상담 이력 (DB 연동 전)
const dummyConsults = [
  { id: 1, date: '2024-05-01', type: '세무기장', status: '처리중' },
  { id: 2, date: '2024-04-20', type: '세무자문', status: '완료' }
];

router.get('/', (req, res) => {
  // 로그인 안 한 경우 로그인으로 리디렉션
  if (!req.session.user) {
    return res.redirect('/login');
  }

  res.render('customer/consult', {
    title: '상담 내역',
    consults: dummyConsults
  });
});

module.exports = router;