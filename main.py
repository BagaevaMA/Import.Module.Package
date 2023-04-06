from datetime import datetime

from application.salary import calculate_salary
from application.people import get_employees

def current_datetime():
    cd = datetime.now()
    print(cd)
    return

if __name__ == '__main__':
    calculate_salary()
    get_employees()
    current_datetime()
