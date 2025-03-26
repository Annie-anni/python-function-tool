import unittest
from city_function import get_cities

class CityTestCase(unittest.TestCase):
    def test_city_country_cities(self):
        cities = get_cities('shanghai','china')
        self.assertEqual(cities,'Shanghai China')

    def test_city_country_population_cities(self):
        cities = get_cities('beijing','china','1,400,000')
        self.assertEqual(cities,'Beijing China 1,400,000')

if __name__ == '__main__':
    unittest.main()