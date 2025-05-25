const express = require('express');
const router = express.Router();
const axios = require('axios');

// 마이페이지 조회
router.get('/', async (req, res) => {
  if (!req.session.token) {
    return res.redirect('/login');
  }

  try {
    const response = await axios.get('http://localhost:8000/customer/mypage', {
      headers: {
        Authorization: `Bearer ${req.session.token}`
      }
    });

    const user = response.data;

    res.render('customer/mypage', {
      title: '마이페이지',
      user
    });
  } catch (error) {
    console.error('[마이페이지 조회 실패]', error.message);
    res.redirect('/login');
  }
});

// 마이페이지 수정 폼
router.get('/edit', async (req, res) => {
  if (!req.session.token) {
    return res.redirect('/login');
  }

  try {
    const response = await axios.get('http://localhost:8000/customer/mypage', {
      headers: {
        Authorization: `Bearer ${req.session.token}`
      }
    });

    const user = response.data;

    res.render('customer/mypage-edit', {
      title: '회원 정보 수정',
      user
    });
  } catch (error) {
    console.error('[회원정보 수정 폼 오류]', error.message);
    res.redirect('/login');
  }
});

// 마이페이지 수정 요청
router.post('/edit', async (req, res) => {
  if (!req.session.token) {
    return res.redirect('/login');
  }

  try {
    // 🔥 여기가 핵심입니다: 타입 변환
    req.body.is_company = req.body.is_company === 'true';
    req.body.company_id = req.body.company_id ? parseInt(req.body.company_id) : null;

    // 🔥 생년월일 YYYYMMDD → YYYY-MM-DD 변환
    if (req.body.birthdate?.length === 8) {
      req.body.birthdate = `${req.body.birthdate.slice(0, 4)}-${req.body.birthdate.slice(4, 6)}-${req.body.birthdate.slice(6, 8)}`;
    }

    await axios.put('http://localhost:8000/customer/mypage', req.body, {
      headers: {
        Authorization: `Bearer ${req.session.token}`
      }
    });

    res.redirect('/mypage');
  } catch (error) {
    console.error('[회원정보 수정 실패]', error.message);
    res.render('customer/mypage-edit', {
      title: '회원 정보 수정',
      user: req.body,
      error: '회원정보 수정에 실패했습니다.'
    });
  }
});

module.exports = router;