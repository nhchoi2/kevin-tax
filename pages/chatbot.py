import streamlit as st
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os
from pinecone import Pinecone, ServerlessSpec

# 1. 환경 변수 로드 (.env 파일)
load_dotenv()
api_key = os.getenv("HUGGINGFACE_API_KEY")
pinecone_api_key = os.getenv("PINECONE_API_KEY")
pinecone_env = os.getenv("PINECONE_ENV")
pinecone_index_name = os.getenv("PINECONE_INDEX_NAME")
pinecone_cloud = os.getenv("PINECONE_CLOUD")  # 예: 'aws'

# 2. Hugging Face API 클라이언트 초기화
# - 채팅 응답용: google/gemma-2-9b-it 모델
client = InferenceClient(provider="hf-inference", api_key=api_key)
# - 임베딩 생성용: sentence-transformers/all-MiniLM-L6-v2 모델
embedding_client = InferenceClient(model="sentence-transformers/all-MiniLM-L6-v2", api_key=api_key)

# 3. Pinecone 인스턴스 생성 (최신 인터페이스 사용)
pc = Pinecone(api_key=pinecone_api_key)
# Pinecone 인덱스가 존재하는지 확인하고, 없으면 생성 (all-MiniLM-L6-v2 임베딩 차원은 384)
if pinecone_index_name not in [idx.name for idx in pc.list_indexes()]:
    pc.create_index(
        name=pinecone_index_name,
        dimension=384,
        metric='cosine',
        spec=ServerlessSpec(cloud=pinecone_cloud, region=pinecone_env)
    )
# 인덱스 연결
index = pc.Index(pinecone_index_name)

# 4. Streamlit UI 설정
st.set_page_config(page_title="헷GPT", page_icon="💬", layout="wide")

# 사이드바: 설정 및 대화 기록 초기화
with st.sidebar:
    st.header("📌 설정")
    clear_chat = st.button("💬 대화 기록 초기화")
    if clear_chat:
        st.session_state.chat_history = []
        st.success("대화 기록이 초기화되었습니다.")

# 메인 타이틀 및 설명
st.title("💬 똑똑한 AI 헷GPT")
st.write("질문을 입력하면 헷GPT가 답변해드립니다.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

def get_embedding(text):
    result = embedding_client.feature_extraction(text)
    # 만약 결과가 numpy ndarray라면 리스트로 변환합니다.
    if hasattr(result, "tolist"):
        result = result.tolist()
    # 만약 다중 토큰 임베딩 리스트라면, 첫 번째 토큰의 임베딩을 사용합니다.
    if isinstance(result, list) and isinstance(result[0], list):
        return result[0]
    return result

def query_pinecone(query_text, top_k=3):
    """
    입력 질문의 임베딩을 생성한 후, Pinecone 인덱스에서 유사 문서를 검색합니다.
    """
    embedding = get_embedding(query_text)
    if embedding is None:
        return None
    results = index.query(vector=embedding, top_k=top_k, include_metadata=True)
    return results

def get_response():
    """
    사용자의 입력과 Pinecone에서 검색된 컨텍스트를 기반으로,
    google/gemma-2-9b-it 모델을 호출하여 답변을 생성합니다.
    """
    user_input = st.session_state.chat_input
    if user_input:
        with st.spinner("헷GPT가 답변을 생성 중입니다..."):
            # Pinecone에서 관련 컨텍스트 검색
            results = query_pinecone(user_input)
            context = ""
            if results and "matches" in results:
                for match in results["matches"]:
                    context += match["metadata"].get("text", "") + "\n"
            # 컨텍스트와 질문을 결합한 프롬프트 구성
            
            prompt = f"Context:\n{context}\n\nQuestion: {user_input}\nAnswer:"
            # 채팅 응답 생성 (google/gemma-2-9b-it 모델 사용)
            response = client.chat.completions.create(
                model="google/gemma-2-9b-it",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1024,
            ).choices[0].message.content
            # 대화 기록 업데이트 (최신 메시지가 위에 표시되도록)
            st.session_state.chat_history.insert(0, ("👤 사용자:", user_input))
            st.session_state.chat_history.insert(0, ("🤖 헷GPT:", response))
            st.session_state.pop("chat_input", None)

# 대화 기록 출력 (최신 메시지가 위쪽에 보이도록 역순 출력)
st.markdown("### 대화 기록")
for role, message in reversed(st.session_state.chat_history):
    st.markdown(f"**{role}** {message}")

# 채팅 입력 필드: 입력 후 get_response 함수 호출
st.chat_input("질문을 입력하세요:", key="chat_input", on_submit=get_response)
