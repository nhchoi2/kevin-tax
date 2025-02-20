import streamlit as st
import pandas as pd


# 페이지 설정: 제목 및 레이아웃 지정
st.set_page_config(
    page_title="KEVIN TAX - 세무 컨설팅",
    layout="wide"
)

# ---------------------- Custom CSS 설정 ----------------------
# 심플하고 전문적인 디자인을 위해, 화이트 배경에 블루/네이비 포인트 컬러와 고급 폰트를 적용합니다.
st.markdown("""
    <style>
    body {
        font-family: 'Pretendard', 'Noto Sans', sans-serif;
        background-color: #ffffff;
    }
    /* 헤더 로고 중앙 배치 */
    .header-logo {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 200px;
    }
    /* 메인 배너 스타일 */
    .main-banner {
        padding: 2rem 0;
    }
    /* 서비스 카드 스타일 */
    .service-card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 8px;
        text-align: center;
        margin: 0.5rem;
    }
    /* 상담 신청 버튼 스타일 */
    .consult-btn {
        background-color: #003366;
        color: #ffffff;
        padding: 0.75rem 1.5rem;
        border: none;
        border-radius: 4px;
        font-size: 1.2rem;
        cursor: pointer;
        text-decoration: none;
    }
    </style>
    """, unsafe_allow_html=True)

# ---------------------- 헤더: 로고 배치 ----------------------
# st.image()를 사용하여 중앙에 KEVIN TAX 로고를 표시합니다.
st.image("data/images/logo.png", width=200)  # 로고 이미지를 중앙에 배치합니다.

# ---------------------- 메인 배너: 세무사 프로필 ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
with st.container():
    # 좌측: 텍스트 정보, 우측: 세무사 사진
    cols = st.columns([2, 1])
    with cols[0]:
        st.markdown("<h2>KEVIN TAX 세무 컨설팅</h2>", unsafe_allow_html=True)
        st.markdown("<h3>홍길동 세무사</h3>", unsafe_allow_html=True)
        st.markdown("<p>전문 분야: 법인 세무, 소득세, 양도세 절세 컨설팅</p>", unsafe_allow_html=True)
        st.markdown("<p>연락처: 010-1234-5678 | 이메일: hong@govtax.com</p>", unsafe_allow_html=True)
        st.markdown("<p><em>신뢰와 전문성을 바탕으로, 최적의 세무 솔루션을 제공합니다.</em></p>", unsafe_allow_html=True)
    with cols[1]:
        st.image("data/images/profile.png", caption="홍길동 세무사", use_container_width=True)

# ---------------------- 주요 서비스 섹션 ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3>주요 서비스</h3>", unsafe_allow_html=True)

# 서비스 항목 설정 (예: 법인 컨설팅, 양도세 절세, 소득세 신고, 세무 자문)
service_names = ["법인 컨설팅", "양도세 절세", "소득세 신고", "세무 자문"]
service_descriptions = [
    "기업의 세무 문제를 체계적으로 해결해 드립니다.",
    "최적의 절세 전략으로 양도세 부담을 줄여드립니다.",
    "정확한 소득세 신고와 절세 방안을 제공합니다.",
    "세무 관련 모든 문제에 대해 전문 상담을 제공합니다."
]
service_icons = ["data/images/icon1.png", "data/images/icon2.png", "data/images/icon3.png", "images/icon4.png"]  # 각 서비스에 사용할 아이콘 이미지 파일

# 4개의 서비스를 4열로 그리드 형식 배치
cols = st.columns(4)
for i, col in enumerate(cols):
    with col:
        # 각 서비스 카드를 위한 div 생성 (CSS 스타일 적용)
        st.markdown("<div class='service-card'>", unsafe_allow_html=True)
        st.image(service_icons[i], width=64)  # 아이콘 이미지 표시
        st.markdown(f"<h4>{service_names[i]}</h4>", unsafe_allow_html=True)
        st.markdown(f"<p>{service_descriptions[i]}</p>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ---------------------- 1:1 상담 신청 버튼 ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3>상담 신청</h3>", unsafe_allow_html=True)
# 상담 신청 버튼: 클릭 시 Consulting.py 페이지로 이동 (링크 형식으로 구현)
st.markdown("""
    <a href="Consulting.py" class="consult-btn">1:1 상담 신청</a>
    """, unsafe_allow_html=True)

# ---------------------- 회사 위치 및 연락처 ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h3>회사 위치 및 연락처</h3>", unsafe_allow_html=True)
# 회사 주소 및 연락처 정보 표시
st.markdown("<p>주소: 서울특별시 송파구 송파대로22길 5-20, 1층 101호 THE KEVIN's TAX</p>", unsafe_allow_html=True)
st.markdown("<p>전화: 02-403-0601 | 이메일: akathekevin@thekevintaxlab.com</p>", unsafe_allow_html=True)

# 지도 표시: st.map()를 사용하여 간단한 지도를 표시 (예: 회사 위치 좌표 사용)
# 서울 강남구의 예시 좌표 (위도, 경도)
location_data = pd.DataFrame({
    'lat': [37.488538],
    'lon': [127.122050]
})
st.map(location_data, use_container_width=True)

# ---------------------- 최종 안내 문구 ----------------------
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>KEVIN TAX - 신뢰와 전문성의 세무 컨설팅</p>", unsafe_allow_html=True)
