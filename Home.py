import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="KEVIN-TAX",
    page_icon="💼",
    layout="wide"
)

# 타이틀
st.title("💼 KEVIN-TAX: AI 기반 세무 상담 서비스")
st.write("환영합니다! KEVIN-TAX에서 AI와 함께 쉽고 빠르게 세무 상담을 받아보세요.")


# 추가적인 메인 콘텐츠 (예: 이미지, 소개 문구 등)
st.markdown("---")
st.subheader("🛠 주요 기능 소개")
st.write("- **📝 상담 신청**: 온라인으로 세무 상담을 요청하세요.")
st.write("- **📊 세금 계산기**: AI 기반 예상 세금 계산 기능 (추후 추가 예정)")
st.write("- **📰 최신 세무 정보**: 세법 및 절세 전략 뉴스 제공 (추후 추가 예정)")

# 푸터
st.markdown("---")
st.markdown("© 2025 KEVIN-TAX. All rights reserved.")
