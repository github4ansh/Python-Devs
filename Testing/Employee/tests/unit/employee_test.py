import unittest
from employee import Employee
from unittest.mock import Mock, patch


class EmployeeTest(unittest.TestCase):

    def test_invalid_email(self):
        with self.assertRaises(ValueError):
            Employee(first='Ansh', last='Stephen', pay=2000, mail='ansh_test')

    def test_print_full_name(self):
        expected_output = 'Ansh Stephen'
        e1 = Employee(first='Ansh', last='Stephen', pay=2000, mail='ansh@blabs.com')
        with patch('builtins.print') as mocked_print:
            actual_full_name = e1.print_fullname()
            mocked_print.assert_called_with(expected_output)
            self.assertEqual(expected_output, actual_full_name)

    def test_expected_salary_hike_input(self):
        hike_prompt = "What's your expected hike percentage"
        expected_hike = 2.0
        e1 = Employee(first='Ansh', last='Stephen', pay=2000, mail='ansh@blabs.com')
        # mock using patch
        with patch('builtins.input') as mocked_input:
            # dynamic values assignation as part of side effects
            mocked_input.side_effect = (1, 2.0)
            actual_hike = e1.expected_salary_hike()
            mocked_input.assert_called_with(hike_prompt)
            self.assertEqual(actual_hike, expected_hike)


if __name__ == '__main__':
    unittest.main()
