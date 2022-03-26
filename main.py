import re

delimiter_flag = "//"
delimiters = ",|\n"


def add(input_str):
    if input_str is None:
        return None
    else:
        if len(input_str) == 0:
            return 0
        else:
            has_delimiter = any(delimiter in input_str for delimiter in delimiters)
            has_custom_delimiter = delimiter_flag in input_str

            if not has_custom_delimiter and not has_delimiter:
                return int(input_str)

            elif has_custom_delimiter:
                custom_delimiter = input_str[2]
                input_str = input_str[3:]
                return array_addition(input_str, custom_delimiter)

            elif has_delimiter:
                return array_addition(input_str)


def array_addition(input_str, delis=None):
    if delis is None:
        numbers = re.split(delimiters, input_str)
    else:
        numbers = input_str.split(delis)
    addition = 0
    for n in numbers:
        addition += int(n)
    return addition


if __name__ == '__main__':
    print(add("//?\n1?2,1"))
