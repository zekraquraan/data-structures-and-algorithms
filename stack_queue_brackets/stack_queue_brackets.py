from collections import deque


def validate_brackets(string):
    """
    Validate whether the brackets in a given string are balanced.

    Args:
        string (str): The input string to check for balanced brackets.

    Returns:
        bool: True if the brackets are balanced, False otherwise.

    Examples:
        >>> validate_brackets("{}")
        True

        >>> validate_brackets("{}(){}")
        True

        >>> validate_brackets("()[[Extra Characters]]")
        True

        >>> validate_brackets("(){}[[]]")
        True

        >>> validate_brackets("{}{Code}[Fellows](())")
        True

        >>> validate_brackets("[({}]")
        False

        >>> validate_brackets("(](")
        False

        >>> validate_brackets("{(})")
        False
    """

    stack = []
    queue = deque()

    opening_brackets = {'(', '[', '{'}
    closing_brackets = {')', ']', '}'}
    bracket_pairs = {'(': ')', '[': ']', '{': '}'}

    for char in string:
        if char in opening_brackets:
            stack.append(char)
            queue.append(char)
        elif char in closing_brackets:
            if not stack:
                return False
            last_opening_bracket = stack.pop()
            if bracket_pairs[last_opening_bracket] != char:
                return False
            queue.append(char)
    
    return len(stack) == 0 and len(queue) % 2 == 0
