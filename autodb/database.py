from sqlalchemy import create_engine, text

# 1. DB 연결 엔진 만들기 (DB 주소를 받아서 연결 통로를 준비함)
def get_engine(db_url: str = "sqlite:///./my_test.db"):
    # SQLite는 주소 뒤에 파일 경로를 적으면 그 위치에 파일을 만듭니다.
    return create_engine(db_url)

# 2. 테스트용 데이터 생성 (Scott 스타일)
def create_test_data(engine):
    with engine.connect() as conn:
        # (1) 기존에 users 테이블이 있다면 삭제 (초기화)
        conn.execute(text("DROP TABLE IF EXISTS users"))
        
        # (2) users 테이블 생성
        conn.execute(text("""
            CREATE TABLE users (
                id INTEGER PRIMARY KEY,
                name TEXT,
                role TEXT,
                salary INTEGER
            )
        """))
        
        # (3) 테스트 데이터 삽입
        conn.execute(text("INSERT INTO users (name, role, salary) VALUES ('Scott', 'Manager', 5000)"))
        conn.execute(text("INSERT INTO users (name, role, salary) VALUES ('Tiger', 'Developer', 4500)"))
        conn.execute(text("INSERT INTO users (name, role, salary) VALUES ('Gemini', 'AI Teacher', 9999)"))
        
        # 데이터 변경을 확정 짓습니다. (매우 중요!)
        conn.commit()
    print("✅ 테스트 DB와 데이터가 생성되었습니다.")