def extract_numbers(input_string):
    result = ""
    for char in input_string:
        if char.isdigit():
            result += char
    return result
