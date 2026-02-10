from stack import Stack 
from datetime import datetime 

def validate(json_string):
    stack = Stack()
    line = 1
    col = 0 

    for char in json_string:
        col += 1 

        # how to handle the new line 
        if char == "\n":
            line += 1
            col = 0 
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
                    f"Mismatched '{open_char}' opened at "
                    f"Line {open_line}, Col {open_col} "
                    f"but found '{char}' at Line {line}, Col {col}"
                )
            
    # after every character has been checked 
    if not stack.is_empty():
        open_char, open_line, open_col = stack.pop()
        return (
            False,
            f"Unexpected '{open_char}' at Line {open_line}, Col {open_col}"
        )
    
    return True, "Valid JSON"