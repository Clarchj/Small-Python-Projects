import unittest
from employee import employee

class GiveRaiseTest(unittest.TestCase):
        def setUp(self):
                """Create an employee instance to use in all test methods
                """
                self.my_employee=employee('Jane','Doe',5000)
        def test_give_default_raise(self):
                """Testing  if the dunction working as intended
                """
                testing_give_raise=self.my_employee.give_raise()
                self.assertEqual(testing_give_raise,"Current salary: 10000$")
        def test_give_custom_raise(self):
                """Testing  if the dunction working as intended
                """
                testing_give_raise=self.my_employee.give_raise(7000)
                self.assertEqual(testing_give_raise,"Current salary: 12000$")
        
                
unittest.main()
                