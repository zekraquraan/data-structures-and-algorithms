import unittest
from stack_queue_brackets.stack_queue_brackets import validate_brackets


class ValidateBracketsTestCase(unittest.TestCase):
    def test_validate_brackets(self):
        test_cases = [
            ("{}", True),
            ("{}(){}", True),
            ("()[[Extra Characters]]", True),
            ("(){}[[]]", True),
            ("{}{Code}[Fellows](())", True),
            ("[({}]", False),
            ("(](", False),
            ("{(})", False),
            ("{", False),
            (")", False),
            ("[}", False),
        ]

        for i, (input_string, expected_output) in enumerate(test_cases):
            with self.subTest(test_number=i+1):
                result = validate_brackets(input_string)
                self.assertEqual(result, expected_output, f"Test case {i+1} failed")

        print("All test cases passed!")


if __name__ == '__main__':
    unittest.main()
