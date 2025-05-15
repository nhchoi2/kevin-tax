// 📌 public/js/service.js

// 사이드바 메뉴 클릭 시 해당 섹션으로 스크롤 이동
const sidebarLinks = document.querySelectorAll('.service-sidebar a');

sidebarLinks.forEach(link => {
  link.addEventListener('click', function (e) {
    e.preventDefault();
    const targetId = this.getAttribute('href');
    const targetEl = document.querySelector(targetId);
    if (targetEl) {
      window.scrollTo({
        top: targetEl.offsetTop - 80, // 상단 여백 보정
        behavior: 'smooth'
      });
    }
  });
});

// 스크롤 위치에 따라 사이드바 항목 active 클래스 토글
const sections = document.querySelectorAll('.service-card');
window.addEventListener('scroll', () => {
  let scrollPos = window.scrollY || document.documentElement.scrollTop;

  sections.forEach(section => {
    const id = section.getAttribute('id');
    const offsetTop = section.offsetTop - 100;
    const offsetBottom = offsetTop + section.offsetHeight;

    const link = document.querySelector(`.service-sidebar a[href="#${id}"]`);
    if (scrollPos >= offsetTop && scrollPos < offsetBottom) {
      link.classList.add('active');
    } else {
      link.classList.remove('active');
    }
  });
});
