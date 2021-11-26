import os
import unittest

from bank import Employee


class EmployeeRaiseSalaryTestCase(unittest.TestCase):
    def setUp(self):
        self.employee = Employee('Ana Popescu', None, 100)

    def test_raise_salary_valid_percent(self):
        self.employee.raise_salary(10)
        self.assertEqual(self.employee.salary, 110)

    def test_raise_salary_invalid_percent(self):
        with self.assertRaises(ValueError):
            self.employee.raise_salary(50)
        self.assertEqual(self.employee.salary, 100)

    @unittest.skipIf(os.name == 'posix', 'Not running on posix systems')
    def test_raise_negative_percent(self):
        with self.assertRaises(ValueError):
            self.employee.raise_salary(-50)
        self.assertEqual(self.employee.salary, 100)
