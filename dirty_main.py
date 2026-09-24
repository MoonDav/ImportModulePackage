# dirty_main.py
from datetime import datetime
from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    now = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    print(f"=== dirty_main запущен {now} ===")
    calculate_salary()
    get_employees()
