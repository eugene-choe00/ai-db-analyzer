from sqlalchemy import create_engine, text

def get_db_connection(db_url: str):
    """
    DB URL을 받아 연결 엔진을 생성합니다.
    예: sqlite:///./test.db
    """
    engine = create_engine(db_url)
    return engine

def check_connection(engine):
    """
    연결이 잘 되었는지 테스트 쿼리를 날려봅니다.
    """
    try:
        with engine.connect() as connection:
            # "1"을 선택하는 아주 간단한 쿼리를 날려봅니다.
            connection.execute(text("SELECT 1"))
        return True
    except Exception as e:
        print(f"연결 실패: {e}")
        return False