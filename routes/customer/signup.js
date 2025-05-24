const express = require('express');
const axios = require('axios');
const router = express.Router();

// 날짜 형식 변환 함수: '19850524' → '1985-05-24'
function formatBirthdate(raw) {
  if (raw.length === 8) {
    const y = raw.slice(0, 4);
    const m = raw.slice(4, 6);
    const d = raw.slice(6, 8);
    return `${y}-${m}-${d}`;
  }
  return raw;
}

// 회원가입 페이지
router.get('/', (req, res) => {
  res.render('customer/signup', {
    title: '회원가입 | 케빈택스',
    error: null,
  });
});

// 회원가입 POST 처리
router.post('/', async (req, res) => {
  const {
    name,
    email,
    password,
    confirmPassword,
    phone,
    birthdate,
    gender,
    agree,
  } = req.body;

  // 비밀번호 일치 확인
  if (password !== confirmPassword) {
    return res.render('customer/signup', {
      title: '회원가입 | 케빈택스',
      error: '비밀번호가 일치하지 않습니다.',
    });
  }

  // 개인정보 동의 체크 확인
  if (!agree) {
    return res.render('customer/signup', {
      title: '회원가입 | 케빈택스',
      error: '개인정보 수집 및 이용에 동의해야 가입이 가능합니다.',
    });
  }

  try {
    const response = await axios.post('http://127.0.0.1:8000/customer/signup', {
      name,
      email,
      password,
      phone,
      birthdate: formatBirthdate(birthdate), // ← ✅ 날짜 형식 변환 적용
      gender,
      postal_code: '',
      address1: '',
      address2: '',
      is_company: false,
      company_id: null,
      privacy_agreed: true,
    });

    // ✅ 성공 시 팝업 후 로그인 페이지 이동
    res.send(`
      <script>
        alert("회원가입이 완료되었습니다.");
        window.location.href = "/login";
      </script>
    `);
  } catch (err) {
    console.error('회원가입 오류:', err.response?.data || err.message);
    const errorMessage = err.response?.data?.detail || '회원가입에 실패했습니다.';
    res.render('customer/signup', {
      title: '회원가입 | 케빈택스',
      error: errorMessage,
    });
  }
});

module.exports = router;