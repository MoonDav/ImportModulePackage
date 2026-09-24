# dirty_main.py
from datetime import datetime
from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(f"=== dirty_main запущен {datetime.now().strftime('%d.%m.%Y %H:%M:%S')} ===")
    calculate_salary()
    get_employees()
