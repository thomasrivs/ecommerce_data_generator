from datetime import datetime


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
        if datetime(self.year, self.month, self.day).weekday() > 0:
            total_visits = random.randint(5000, 10000)
        else:
            total_visits = random.randint(7000, 15000)

        return total_visits



