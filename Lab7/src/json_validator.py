from stack import Stack 
from datetime import datetime 

def validate(json_string):
    stack = Stack()
    line = 1
    col = 0 
    in_string = False
    leave_next = False

    for char in json_string:
        col += 1 

        # how to handle the new line 
        if char == "\n":
            line += 1
            col = 0 
            continue 

        # string mode 
        if in_string:
            if leave_next:
                leave_next = False
                continue
            
            if char == "\\":
                leave_next = True 
                continue

            if char == '"':
                in_string = False 

            # ignores everything else inside the strings 
            continue

        # normal mode 
        if char == '"':
            in_string = True 
            continue 

        # handles the opening characters 
        if char == "{" or char == "[":
            stack.push((char, line, col))

        # handles the closing characters 
        elif char == "}" or char == "]":
            if stack.is_empty():
                return (
                    False,
                    f"Unexpected '{char}' at Line {line}, Col {col}"
                )
            
            open_char, open_line, open_col = stack.pop()

            # checks for any messed up pairs 
            if (open_char == "{" and char != "}") or (
                open_char == "[" and char != "]"
            ):
                return (
                   False,
                    f"Expected matching closer for '{open_char}' "
                    f"(opened at Line {open_line}, Col {open_col}) "
                    f"but found '{char}' at Line {line}, Col {col}"
                )
    
    # checks the input 
    if in_string:
        return False, "Unterminated string"
    
    # after every character has been checked 
    if not stack.is_empty():
        open_char, open_line, open_col = stack.pop()
        return (
            False,
            f"Unexpected '{open_char}' at Line {open_line}, Col {open_col}"
        )
    
    return True, "Valid JSON"