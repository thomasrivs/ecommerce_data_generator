import unittest

from app import read_sales_data

class TestReadSalesData(unittest.TestCase):
    def test_read_sales_data(self):
        self.assertEqual(read_sales_data(0), 1)

if __name__ == '__main__':
    unittest.main()
