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