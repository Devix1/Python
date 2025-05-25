import unittest
from app import convert_currency  

class TestCurrencyConverter(unittest.TestCase):

    def test_usd_to_eur(self):
        self.assertEqual(convert_currency(100, 'USD', 'EUR'), 92.0)

    def test_eur_to_usd(self):
        self.assertEqual(convert_currency(100, 'EUR', 'USD'), 109.0)

    def test_rub_to_usd(self):
        self.assertEqual(convert_currency(1000, 'RUB', 'USD'), 11.0)

    def test_same_currency(self):
        self.assertEqual(convert_currency(50, 'USD', 'USD'), 50)

    def test_invalid_currency_pair(self):
        with self.assertRaises(ValueError):
            convert_currency(100, 'USD', 'ABC')  

if __name__ == '__main__':
    unittest.main()
