from stack import Stack 
from json_validator import validate

def validate(json_string):
    # Initialize line and column counters
    line = 1
    col = 0

    # ── STATE FLAG ───────────────────────────────────────────────
    # in_string tracks whether we are currently inside a quoted string.
    # While True, structural characters like { and [ are ignored.
    in_string = False

    for character in json_string:
        col += 1

        if character == "\n":
            line += 1
            col = 0
            continue

        # ── STRING MODE ──────────────────────────────────────────
        # When inside a string, only escapes and closing quotes matter.
        if in_string:
            if character == "\\":
                # Skip the next character (escaped)
                continue
            elif character == '"':
                in_string = False
            continue

        # ── NORMAL MODE ──────────────────────────────────────────
        # We are outside of any string.

        if character == '"':
            in_string = True
            continue

        # Opening brace or bracket
        if character == "{" or character == "[":
            stack.push((character, line, col))

        # Closing brace or bracket
        elif character == "}" or character == "]":
            if stack.is_empty():
                # Unexpected closing character
                return False, f"ERROR Line {line}, Col {col}: unexpected closer"

            open_char, open_line, open_col = stack.pop()

            if (open_char == "{" and character != "}") or \
                (open_char == "[" and character != "]"):
                return (
                    False,
                    f"ERROR Line {line}, Col {col}: expected matching closer for "
                    f"'{open_char}' opened at Line {open_line}, Col {open_col}"
                )

    # ── AFTER ALL CHARACTERS ─────────────────────────────────────

    if in_string:
        return False, "ERROR: unterminated string"

    if not stack.is_empty():
        open_char, open_line, open_col = stack.pop()
        return False, f"ERROR: unclosed '{open_char}' at Line {open_line}, Col {open_col}"

    return True, "VALID"