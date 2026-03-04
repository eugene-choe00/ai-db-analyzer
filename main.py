# test grass
import typer
from rich.console import Console
from autodb import database  # 우리가 만든 database.py를 가져옵니다.
from autodb import ai_analyzer
from autodb.database import get_engine, get_all_users

app = typer.Typer()
console = Console()

@app.command()
def hello():
    """인사하는 명령어"""
    console.print("[bold cyan]안녕하세요, 맹구님![/bold cyan] AI DB 분석기 프로젝트에 오신 걸 환영합니다. 🚀")

@app.command()
def version():
    """버전 확인 명령어"""
    console.print("AI DB Analyzer Version: [bold]0.1.0[/bold]")

@app.command()
def setup_db():
    """테스트용 SQLite DB를 생성하고 데이터를 채웁니다."""
    engine = database.get_engine()
    with console.status("[bold yellow]DB 생성 중..."):
        database.create_test_data(engine)
    console.print("[bold green]준비 완료! 'my_test.db' 파일이 생성되었습니다.[/bold green]")

@app.command()
def ask(question: str):
    """AI에게 궁금한 점을 물어보는 명령어"""
    with console.status("[bold yellow]Gemini가 생각 중..."):
        answer = ai_analyzer.ask_gemini(question)
    console.print(f"\n[bold magenta]AI 답변:[/bold magenta]\n{answer}")

@app.command()
def analyze():
    """DB에 있는 사용자 목록을 읽어와서 AI에게 분석을 요청합니다."""
    engine = get_engine()
    
    with console.status("[bold yellow]DB에서 데이터를 읽고 분석하는 중..."):
        # 1. DB에서 모든 사용자 정보 가져오기
        users = get_all_users(engine)
        
        if not users:
            console.print("[bold red]분석할 데이터가 DB에 없습니다. 먼저 'setup-db'를 실행하세요.[/bold red]")
            return

        # 2. AI가 이해하기 쉽게 텍스트로 변환 (프롬프트 구성)
        user_list_str = "\n".join([f"- 이름: {u.name}, 역할: {u.role}" for u in users])
        prompt = f"""
        다음은 우리 데이터베이스에 등록된 사용자들의 목록이야:
        {user_list_str}
        
        이 데이터를 보고 우리 팀의 구성 특징을 분석해서 보고서 형태로 짧게 요약해줘.
        """

        # 3. AI에게 질문 던지기
        analysis_result = ai_analyzer.ask_gemini(prompt)

    console.print("\n[bold green]📊 AI의 데이터 분석 보고서:[/bold green]")
    console.print(f"------------------------------------------\n{analysis_result}")


if __name__ == "__main__":
    app()