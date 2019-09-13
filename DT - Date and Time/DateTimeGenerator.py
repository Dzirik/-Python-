import random
from datetime import datetime


def is_leap(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


class DateTimeGenerator():

    def __init__(self):
        pass

    @staticmethod
    def generate_year(year_from=1900, year_to=datetime.now().year):
        return random.randint(year_from, year_to)

    @staticmethod
    def generate_month(month_from=1, month_to=12):
        return random.randint(month_from, month_to)

    @staticmethod
    def generate_day(year, month):
        day_from = 1
        if month in {1, 3, 5, 7, 8, 10, 12}:
            day_to = 31
        elif month in {4, 6, 9, 11}:
            day_to = 30
        if month == 2:
            if is_leap(year):
                day_to = 29
            else:
                day_to = 28

        return random.randint(day_from, day_to)

    def generate_date(self, year_from=1900, year_to=datetime.now().year,
                      month_from=1, month_to=12):
        year = self.generate_year(year_from, year_to)
        month = self.generate_month(month_from, month_to)
        day = self.generate_day(year, month)

        return (year, month, day)
