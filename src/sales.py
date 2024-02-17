from datetime import datetime
from numpy import random


class Sales():
    def __init__(self, year, month, day, hour):
        # Treatment of the year:
        if year > datetime.today().year:
            raise ValueError("You are in the future my friend!")
        elif year < 2020:
            raise ValueError("No data available before 2020!")
        else:
            self.year = year

        # Treatment of the month:
        if 1 <= month <= 12:
            self.month = month
        else:
            raise ValueError("Please enter correct month")

        # Treatment of the year:
        if 1 <= day <= 31:
            self.day = day
        else:
            raise ValueError("Please enter correct day")

        # Treatment of the year:
        if 0 <= hour <= 59:
            self.hour = hour
        else:
            raise ValueError("Please enter correct hour")

    def get_visits_on_the_website(self):
        # JOUR DE SEMAINE NUIT
        if 1 <= datetime(self.year, self.month, self.day).weekday() <= 5 & 0 <= datetime(self.year, self.month,
                                                                                         self.day, self.hour).hour <= 7:
            total_visits = random.randint(200, 1000)

            # JOUR DE SEMAINE JOUR
        elif 1 <= datetime(self.year, self.month, self.day).weekday() <= 5 & 8 <= datetime(self.year, self.month,
                                                                                           self.day,
                                                                                           self.hour).hour <= 23:
            total_visits = random.randint(2000, 8000)

            # WEEK_END NUIT
        elif datetime(self.year, self.month, self.day).weekday() == 6 | 0 & 0 <= datetime(self.year, self.month,
                                                                                          self.day,
                                                                                          self.hour).hour <= 7:
            total_visits = random.randint(5000, 10000)

            # WEEK_END JOUR
        elif datetime(self.year, self.month, self.day).weekday() == 6 | 0 & 8 <= datetime(self.year, self.month,
                                                                                          self.day,
                                                                                          self.hour).hour <= 23:
            total_visits = random.randint(5000, 10000)

        return total_visits



