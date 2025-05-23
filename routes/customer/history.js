const express = require('express');
const router = express.Router();

// 임시 상담 내역 (DB 연동 전)
const dummyConsults = [
  { id: 1, title: '부가세 신고 상담', status: '완료', date: '2024-04-20' },
  { id: 2, title: '종합소득세 문의', status: '처리중', date: '2024-05-02' }
];

router.get('/', (req, res) => {
  const user = req.session.user;
  if (!user) return res.redirect('/login');

  res.render('customer/history', {
    title: '상담 신청 내역',
    consults: dummyConsults
  });
});

module.exports = router;