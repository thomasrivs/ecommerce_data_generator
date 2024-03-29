from datetime import datetime
from numpy import random
import numpy as np


class Sales:
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
        if 0 <= hour <= 23:
            self.hour = hour
        else:
            raise ValueError("Please enter correct hour")

    def generate_ecommerce_data(self):

        # Coefficients for indicators
        avg_sessions = random.randint(5000, 15000)
        avg_add_to_cart = int(avg_sessions * random.uniform(0.2, 0.4))
        avg_initiate_checkout = int(avg_sessions * random.uniform(0.1, 0.2))
        avg_conversions = int(avg_sessions * random.uniform(0.01, 0.05))

        data = np.array([avg_sessions, avg_add_to_cart, avg_initiate_checkout, avg_conversions])
        labels = ["sessions", 'add_to_cart', 'initiate_checkout', "sales"]

        # Initialize variables for each condition's effect
        night_factor = 1.0
        weekend_factor = 1.0
        august_factor = 1.0

        # If during the night, we make sure to drop by 60% the metrics
        if self.hour in [22, 23, 0, 1, 2, 3, 4, 5, 6]:
            night_factor = 0.4

        # If during the weekend, we make sure to increase by 15% the metrics
        if datetime(self.year, self.month, self.day, self.hour).weekday() in [6, 0]:
            weekend_factor = 1.15

        # If during August, we make sure to drop by 60% the visits and the performances
        if self.month == 8:
            august_factor = 0.4

        # Apply cumulative factors to data
        temp_data = (data * night_factor * weekend_factor * august_factor).astype(int).tolist()

        final_data = dict(zip(labels, temp_data))
        return final_data
