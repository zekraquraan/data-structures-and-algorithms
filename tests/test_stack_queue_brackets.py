import unittest
from stack_queue_brackets.stack_queue_brackets import validate_brackets
def test_validate_brackets():
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
        result = validate_brackets(input_string)
        assert result == expected_output, f"Test case {i+1} failed"

    print("All test cases passed!")


# Run the test function
test_validate_brackets()
