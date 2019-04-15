import unittest
from employee import employee

class Test_Employee(unittest.TestCase):
    
    def setUp(self):
        self.employee('david', 'brown', 30000)
    
    def Test_give_default_raise(self):
        increment = self.employee.increment
        self.employee.give_raise(increment)
        self.assertIn(35000, self.employee.salary)
    
    def Test_give_custom_raise(self):
        increment = 3000
        self.employee.given_raise(increment)
        self.assertIn(33000, self.employee.salary)
    
unittest.main()