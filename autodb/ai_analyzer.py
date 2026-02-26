import os
#from genai import Client  # 구글의 새로운 라이브러리 방식입니다. (아래 수정 전)
from google import genai  # 'genai' 대신 'google'에서 'genai'를 가져옵니다.
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# 새로운 Client 객체를 생성합니다.
client = genai(api_key=api_key)

def ask_gemini(prompt: str):
    """구글 최신 SDK 표준 방식"""
    try:
        # 모델명은 'gemini-1.5-flash' 그대로 사용합니다.
        response = client.models.generate_content(
            model="gemini-1.5-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI 연결 오류가 발생했습니다: {str(e)}"