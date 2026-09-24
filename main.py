# main.py
from datetime import datetime
from rich.console import Console
from application.salary import calculate_salary
from application.db.people import get_employees


if __name__ == '__main__':
    print(f"=== Бухгалтерия запущена {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
    calculate_salary()
    get_employees()
    print("=== Работа завершена ===")

    console = Console()
    console.print(f"[bold green]Бухгалтерия выполнила свою работу:[/] {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")

