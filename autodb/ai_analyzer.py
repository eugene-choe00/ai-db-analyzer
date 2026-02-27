import os
#from genai import Client  # 구글의 새로운 라이브러리 방식입니다. (아래 수정 전)
from google import genai  # 'genai' 대신 'google'에서 'genai'를 가져옵니다.
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_MODEL = "models/gemini-2.5-flash"
#gemini-3-flash
#gemini-2.5-flash
#gemini-1.5-flash

# 새로운 Client 객체를 생성합니다.(genai 도구 상자 안에 있는 Client 기술자를 호출!)
client = genai.Client(api_key=API_KEY)

def ask_gemini(prompt: str):
    """구글 최신 SDK 표준 방식"""
    try:
        # 모델명을 위에서 정의한 GEMINI_MODEL로 사용합니다.
        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI 연결 오류가 발생했습니다: {str(e)}"   