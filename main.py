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
            if delimiter_flag not in input_str and not has_delimiter:
                return int(input_str)
            else:
                numbers = re.split(delimiters, input_str)
                addition = 0
                for n in numbers:
                    addition += int(n)
                return addition


if __name__ == '__main__':
    print(add("1,4"))
