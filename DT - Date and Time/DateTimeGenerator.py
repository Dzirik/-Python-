import random
from datetime import datetime

class DateTimeGenerator():

    def __init__(self):
        pass

    def generate_year(self, year_from=1900, year_to=datetime.now().year):
        return random.randint(year_from, year_to)

def __is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
