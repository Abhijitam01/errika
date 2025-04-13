import re

ERROR_PATTERNS = [
    re.compile(r"Traceback \(most recent call last\):"),
    re.compile(r"Error:"),
    re.compile(r"Exception:"),
    re.compile(r"^\s*File \".+\", line \d+, in .+"),
    re.compile(r"ModuleNotFoundError:"),
    re.compile(r"NameError:"),
    re.compile(r"SyntaxError:"),
    re.compile(r"TypeError:"),
    re.compile(r"ValueError:"),
]

def is_error_line(line : str) -> bool:
    for pattern in ERROR_PATTERNS:
        if pattern.search(line):
            return True
    return False