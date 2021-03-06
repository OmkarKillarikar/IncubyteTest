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
                negative_present = False
                if int(input_str) < 0:
                    negative_present = True
                    try:
                        raise Exception("negatives not allowed: " + input_str)
                    except Exception as e:
                        print(e)
                if negative_present is not True:
                    return int(input_str)

            elif has_custom_delimiter:
                custom_delimiter = input_str[2]
                input_str = input_str[4:]
                return array_addition(input_str, custom_delimiter)

            elif has_delimiter:
                return array_addition(input_str)


def array_addition(input_str, delis=None):
    if delis is None:
        numbers = re.split(delimiters, input_str)
    else:
        numbers = input_str.split(delis)
    addition = 0
    negative_present = False
    for n in numbers:
        if int(n) < 0:
            try:
                negative_present = True
                raise Exception("negatives not allowed: " + n)
            except Exception as e:
                print(e)
        elif not negative_present:
            addition += int(n)

    if not negative_present:
        return addition


if __name__ == '__main__':
    print(add("//?\n-1?2?-1?-7"))
