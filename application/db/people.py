# application/db/people.py
from datetime import datetime

__all__ = ['get_employees']


def get_employees():
    """Функция для получения списка сотрудников (заглушка)."""
    print(f"[people] Список сотрудников получен. Дата: {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")


if __name__ == '__main__':
    get_employees()
