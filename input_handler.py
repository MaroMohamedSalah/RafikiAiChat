# Removes consecutive duplicate characters from the input string.
#
# Args:
# - input_string (str): The input string to process.
#
# Returns:
# - result (str): Input string without consecutive duplicate characters.


def handle_input(input_string):
    result = ""
    for char in input_string:
        if len(result) == 0 or char != result[-1]:
            result += char
    return result
