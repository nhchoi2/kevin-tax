const express = require('express');
const axios = require('axios');
const router = express.Router();

// 로그인 화면 렌더링
router.get('/', (req, res) => {
  res.render('customer/login', { title: '로그인', error: null });
});

// 로그인 요청 처리
router.post('/', async (req, res) => {
  const { email, password } = req.body;

  try {
    // FastAPI 로그인 API 호출
    const response = await axios.post('http://127.0.0.1:8000/customer/login', {
      email,
      password
    });

    const user = response.data;

    // 세션에 사용자 정보 저장
    req.session.user = {
      id: user.user_id,
      name: user.name,
      email: user.email,
      access_token: user.access_token,
      refresh_token: user.refresh_token,
    };

    // ✅ 마이페이지 라우터에서 사용하는 토큰도 저장
    req.session.token = user.access_token;

    // 로그인 성공 → 홈으로 이동 
    res.redirect('/');
  } catch (err) {
    console.error('로그인 오류:', err.response?.data || err.message);
    const errorMessage = err.response?.data?.detail || '로그인에 실패했습니다.';
    res.render('customer/login', { title: '로그인', error: errorMessage });
  }
});

// 리프레쉬 토큰으로 access_token 갱신 요청
router.post('/refresh-token', async (req, res) => {
  const refresh_token = req.session.user?.refresh_token;

  if (!refresh_token) {
    return res.status(401).send('리프레쉬 토큰이 존재하지 않습니다.');
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/customer/refresh', {
      refresh_token
    });

    // 세션 내 access_token 갱신
    req.session.user.access_token = response.data.access_token;

    return res.status(200).send('Access token 재발급 완료');
  } catch (err) {
    console.error('토큰 갱신 오류:', err.response?.data || err.message);
    return res.status(401).send('토큰 갱신 실패');
  }
});

module.exports = router;