import unittest
from city_function import get_city_function

class CitiesTestCase(unittest.TestCase):
        def test_city_country(self):
                '''' Test if the function work as intended'''
                formatted_cities=get_city_function("ha noi","viet nam")
                self.assertEqual(formatted_cities, "Ha Noi, Viet Nam")
        def test_city_country_population(self):
                '''' Test if the function work as intended'''
                formatted_cities_pop=get_city_function("ha noi","viet nam",5000000)
                self.assertEqual(formatted_cities_pop, "Ha Noi, Viet Nam-Population:5000000")

unittest.main()