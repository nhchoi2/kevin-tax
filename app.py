import streamlit as st
import requests
import os

# .env 파일 로드
from dotenv import load_dotenv
load_dotenv()

# Hugging Face API 키
HF_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
MODEL_NAME = "Qwen/Qwen2.5-Coder-32B-Instruct"
API_URL = f"https://api-inference.huggingface.co/models/{MODEL_NAME}"

# API 요청 함수
def query_huggingface_api(prompt):
    headers = {"Authorization": f"Bearer {HF_API_KEY}"}
    payload = {"inputs": prompt, "parameters": {"max_length": 512, "temperature": 0.7}}

    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# Streamlit UI
st.title("AI 코드 생성 및 실행 (Qwen API)")

# 사용자 입력 (원하는 UI 기능 설명)
user_input = st.text_area("원하는 UI 설명을 입력하세요", "버튼과 입력창이 있는 화면을 만들어줘")

if st.button("코드 생성"):
    with st.spinner("AI가 코드를 생성하는 중..."):
        response = query_huggingface_api(f"Streamlit을 사용하여 {user_input} 기능을 구현하는 Python 코드를 작성해줘.")
        
        # API 응답 처리
        if isinstance(response, dict) and "error" in response:
            st.error(f"API 오류: {response['error']}")
        else:
            generated_code = response[0]["generated_text"]
            st.session_state["generated_code"] = generated_code
            st.code(generated_code, language="python")

# 실행 버튼 (뷰 보기)
if "generated_code" in st.session_state and st.button("뷰 보기"):
    with st.spinner("코드를 실행하는 중..."):
        exec(st.session_state["generated_code"])
