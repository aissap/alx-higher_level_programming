#!/usr/bin/python3



def text_indentation(text):
    """Prints a text with 2 new lines after each '.', '?' and ':'
    Args:
        text: The input text.
    Raises:
        TypeError: If 'text' is not a string."""

        if not isinstance(text, str):
        raise TypeError("text must be a string")

    punctuation = ['.', '?', ':']
    res = ""

    for char in text:
        res += char
        if char in punctuation:
            res += '\n\n'

    lines = result.split('\n')
    clean_lines = [line.strip() for line in lines]
    clean_result = '\n'.join(clean_lines)
    print(clean_result)
