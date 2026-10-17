def is_valid_parentheses(s: str) -> bool:
    """Return True if the brackets in s are balanced."""
    # the stack holds opening brackets that are still waiting to be closed
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}

    for char in s:
        if char in '([{':
            # opening bracket: push it on the stack
            stack.append(char)
        elif char in pairs:
            # closing bracket: the top of the stack must be its match
            if not stack or stack.pop() != pairs[char]:
                return False

    # balanced only if nothing is left waiting
    return len(stack) == 0