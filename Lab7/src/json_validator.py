from stack import Stack

def validate(json_string):
    stack = Stack()
    line = 1
    col = 0
    in_string = False
    i = 0

    while i < len(json_string):
        char = json_string[i]
        col += 1

        # Handle newline
        if char == "\n":
            line += 1
            col = 0
            i += 1
            continue

        # Inside string
        if in_string:
            if char == "\\" and i + 1 < len(json_string):
                # Skip escaped character
                i += 2
                col += 1
                continue
            elif char == '"':
                in_string = False
            i += 1
            continue

        # Outside string
        if char == '"':
            in_string = True
            i += 1
            continue

        # Opening braces/brackets
        if char in "{[":
            stack.push((char, line, col))

        # Closing braces/brackets
        elif char in "}]":
            if stack.is_empty():
                return False, f"ERROR Line {line}, Col {col}: Unexpected '{char}'"

            open_char, open_line, open_col = stack.pop()
            expected = "}" if open_char == "{" else "]"

            if char != expected:
                return (
                    False,
                    f"ERROR Line {line}, Col {col}: Expected matching closer for '{open_char}' "
                    f"(opened at Line {open_line}, Col {open_col}) but found '{char}'"
                )

        i += 1

    # End of file checks
    if in_string:
        return False, f"ERROR Line {line}, Col {col}: Unterminated string"

    if not stack.is_empty():
        open_char, open_line, open_col = stack.pop()
        return False, f"ERROR: Unclosed '{open_char}' at Line {open_line}, Col {open_col}"

    return True, "VALID"