from datetime import datetime
import streamlit as st
import pandas as pd
import os

# ✅ CSS 스타일 추가
st.markdown("""
    <style>
    /* 전체 배경 스타일 */
    .main {
        background-color: #f9f9f9;
        padding: 20px;
        border-radius: 10px;
    }
    
    /* 제목 스타일 */
    .title {
        text-align: center;
        font-size: 32px;
        font-weight: bold;
        color: #2B6CB0;
    }

    /* 상담 신청 폼 스타일 */
    .form-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }

    /* 상담 내역 테이블 헤더 */
    .table-header {
        background-color: #2B6CB0;
        color: white;
        font-weight: bold;
        padding: 8px;
        border-radius: 5px;
    }

    /* 상태 버튼 색상 */
    .pending-button {
        background-color: #FFA500;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }

    .completed-button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 5px 10px;
        border-radius: 5px;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)





# CSV 파일명
CSV_FILE = "consulting_requests.csv"

# 기존 데이터 로드 (없으면 새로 생성)
if os.path.exists(CSV_FILE):
    df = pd.read_csv(CSV_FILE)
else:
    df = pd.DataFrame(columns=["신청 일자", "성명", "연락처", "상담 요청 일자", "상담 내용", "상태"])

# 페이지 제목
st.title("📌 상담 신청 페이지")
st.write("아래 정보를 입력하면 세무 상담을 신청할 수 있습니다.")

# 유저 입력 폼
with st.form("consulting_form"):
    name = st.text_input("성명", "")
    contact = st.text_input("연락처", "")
    request_date = st.date_input("상담 요청 일자")
    details = st.text_area("상담 내용", "")

    submitted = st.form_submit_button("신청하기")

# 제출 시 데이터 저장
if submitted:
    today_date = datetime.today().date()
    new_data = pd.DataFrame(
        [[today_date, name, contact, request_date, details, "대기중"]],
        columns=["신청 일자", "성명", "연락처", "상담 요청 일자", "상담 내용", "상태"]
    )

    df = pd.concat([df, new_data], ignore_index=True)
    df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")  # CSV 파일 저장

    st.success("✅ 상담 신청이 완료되었습니다!")
    st.rerun() 


if not df.empty:
    df["신청 일자"] = pd.to_datetime(df["신청 일자"])  # 신청 일자 컬럼을 날짜 타입으로 변환
    df = df.sort_values(by=["상태", "신청 일자"], ascending=[True, True])  # 상태(대기중 우선) → 신청일자(오래된 순) 정렬
   
    st.subheader("📋 현재 상담 신청 내역")
    header_cols = st.columns([2, 2, 2, 2, 5, 2, 2])
    header_cols[0].write("📅 접수일")
    header_cols[1].write("👤 성명")
    header_cols[2].write("📞 연락처")
    header_cols[3].write("📆 상담일일")
    header_cols[4].write("📝 문의내용")
    header_cols[5].write("🔄 상태")
    header_cols[6].write("🗑️ 삭제")

    for i in range(len(df)):
        col1, col2, col3, col4, col5, col6, col7 = st.columns([2, 2, 2, 2, 5, 2, 2])
        
        col1.write(df.loc[i, "신청 일자"].strftime("%Y-%m-%d"))  # 날짜 형식 변환하여 출력
        col2.write(df.loc[i, "성명"])
        col3.write(df.loc[i, "연락처"])
        col4.write(df.loc[i, "상담 요청 일자"])
        col5.write(df.loc[i, "상담 내용"])
        
        # 상태 업데이트 버튼
        if col6.button(f"{df.loc[i, '상태']}", key=f"status_{i}"):
            df.loc[i, "상태"] = "상담완료" if df.loc[i, "상태"] == "대기중" else "대기중"
            df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")
            st.rerun()  # 새로고침

        # 삭제 버튼
        if col7.button("🗑️", key=f"delete_{i}"):
            df = df.drop(index=i).reset_index(drop=True)
            df.to_csv(CSV_FILE, index=False, encoding="utf-8-sig")
            st.rerun()  # 새로고침

else:
    st.write("📌 현재 상담 신청이 없습니다.")