import unittest
from src.sales import Sales

class TestReadSalesData(unittest.TestCase):
    def test_read_sales_data_old_date(self):
        self.assertEqual(Sales(2028,2,2,1).generate_ecommerce_data(), "You are in the future my friend!")

