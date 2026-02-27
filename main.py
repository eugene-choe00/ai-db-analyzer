# test grass
import typer
from rich.console import Console
from autodb import database  # 우리가 만든 database.py를 가져옵니다.
from autodb import ai_analyzer

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

if __name__ == "__main__":
    app()