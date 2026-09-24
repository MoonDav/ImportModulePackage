# application/db/people.py
from datetime import datetime

__all__ = ['get_employees']


def get_employees():
    """Функция для получения списка сотрудников (заглушка)."""
    now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(f"[people] Список сотрудников получен. Дата: {now}")


if __name__ == '__main__':
    get_employees()
