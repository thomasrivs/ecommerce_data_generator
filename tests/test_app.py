import unittest
from fastapi.testclient import TestClient
from app import app

class TestReadSalesData(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_read_sales_data_invalid_country(self):
        self.assertEqual(self.client.get("/?country=nl&year=2023&month=1&day=12&hour=12").json(),  "error: Invalid country requested")

    def test_read_sales_data_old_date(self):
        self.assertEqual(self.client.get("/?country=fr&year=2018&month=1&day=12&hour=12").json(),  "error: No data before 2020")

    def test_read_sales_data_future_date(self):
        self.assertEqual(self.client.get("/?country=fr&year=2032&month=1&day=12&hour=12").json(),  "error: Please select a correct date")

    def test_read_sales_data_invalid_month(self):
        self.assertEqual(self.client.get("/?country=fr&year=2022&month=32&day=12&hour=12").json(),  "error: Please select a correct date")

    def test_read_sales_data_invalid_day(self):
        self.assertEqual(self.client.get("/?country=fr&year=2022&month=3&day=32&hour=12").json(),  "error: Please select a correct date")

    def test_read_sales_data_invalid_hour(self):
        self.assertEqual(self.client.get("/?country=fr&year=2022&month=3&day=12&hour=34").json(),  "error: Please select a correct hour")

if __name__ == '__main__':
    unittest.main()
