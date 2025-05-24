const express = require('express');
const path = require('path');
const bodyParser = require('body-parser');
const session = require('express-session');

const app = express();

// 세션 설정
app.use(session({
  secret: 'kevin-tax-secret-key',
  resave: false,
  saveUninitialized: true,
  cookie: { maxAge: 1000 * 60 * 60 } // 1시간
}));

// Body parser
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// 정적 파일
app.use(express.static(path.join(__dirname, 'public')));

// 뷰 엔진
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// ✅ 전역 변수 설정: 모든 EJS에서 user 사용 가능
app.use((req, res, next) => {
  res.locals.user = req.session.user || null;
  next();
});

// 라우터
const indexRouter = require('./routes/customer/index');
const blogRouter = require('./routes/customer/blog');
const mapRouter = require('./routes/customer/map');
const applyRouter = require('./routes/customer/apply');  // ✅ 리뷰 경로는 /apply
const serviceRouter = require('./routes/customer/service');
const introRouter = require('./routes/customer/intro');
const customerLoginRouter = require('./routes/customer/login');
const mypageRouter = require('./routes/customer/mypage');
const signupRouter = require('./routes/customer/signup');
const consultRouter = require('./routes/customer/consult');
const historyRouter = require('./routes/customer/history');
const settingsRouter = require('./routes/customer/settings');

// ✨ (선택) 로그아웃 라우터도 추가 시 등록
const logoutRouter = require('./routes/customer/logout');

// 라우터 적용
app.use('/', indexRouter);
app.use('/blog', blogRouter);
app.use('/map', mapRouter);
app.use('/apply', applyRouter);
app.use('/service', serviceRouter);
app.use('/intro', introRouter);
app.use('/login', customerLoginRouter);
app.use('/mypage', mypageRouter);
app.use('/signup', signupRouter);
app.use('/consult', consultRouter);
app.use('/history', historyRouter);
app.use('/settings', settingsRouter);
app.use('/logout', logoutRouter);  // 로그아웃 라우터 경로 등록

// 서버 실행
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ KevinTax server running at http://localhost:${PORT}`);
});