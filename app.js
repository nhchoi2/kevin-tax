// app.js
const express = require('express');
const path = require('path');
const app = express();
const indexRouter = require('./routes/index');
const blogRouter = require('./routes/blog');
const mapRouter = require('./routes/map');
const applyRouter = require('./routes/apply');
const serviceRouter = require('./routes/service');
const introRouter = require('./routes/intro');


// 뷰 엔진 설정
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

// 정적 파일 서빙
app.use(express.static(path.join(__dirname, 'public')));

// 라우터 연결
app.use('/', indexRouter);
app.use('/blog', blogRouter);
app.use('/map', mapRouter);
app.use('/apply', applyRouter);
app.use('/service', serviceRouter);
app.use('/intro', introRouter);

// 서버 실행
const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`✅ KevinTax server running at http://localhost:${PORT}`);
});