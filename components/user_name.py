import re


def extract_user_name(user_input_str):
    name_patterns = [
        re.compile(r"(my name is|I am|name is|I|name) (.+)", re.IGNORECASE),
    ]

    for pattern in name_patterns:
        match = pattern.search(user_input_str)
        if match:
            return match.group(2).strip()

    return None
