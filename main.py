import typer
from rich.console import Console

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

if __name__ == "__main__":
    app()