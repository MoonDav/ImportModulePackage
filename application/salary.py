# application/salary.py
from datetime import datetime

__all__ = ['calculate_salary']


def calculate_salary():
    """Функция для расчёта зарплаты (заглушка)."""
    current_date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(f"[salary] Расчёт зарплаты выполнен. Дата: {current_date}")


if __name__ == '__main__':
    calculate_salary()
