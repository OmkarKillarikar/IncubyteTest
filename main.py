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
                numbers = input_str.split(custom_delimiter)
                addition = 0
                for n in numbers:
                    addition += int(n)
                return addition
            elif has_delimiter and not has_custom_delimiter:
                numbers = re.split(delimiters, input_str)
                addition = 0
                for n in numbers:
                    addition += int(n)
                return addition


if __name__ == '__main__':
    print(add("//?\n1?2,1"))
