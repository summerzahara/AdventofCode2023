from icecream import ic
import re

test_text_2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234",
               "7pqrstsixteen"]

valid_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
convert_valid = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
map_valid_nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


def implement_valid_nums(text):
    new_text = []
    for item in text:
        item_nums = []
        for num in valid_numbers:
            if num in item:
                item_nums.append(num)
                # index = valid_numbers.index(num)
                # item = item.replace(num, convert_valid[index])
        ic(item)
        ic(item_nums)
        # new_text.append(item)
    # return new_text


def calibrate(text):
    result = ""
    for char in text:
        if char.isdigit():
            result += char
            break
    rev_text = text[::-1]
    for char in rev_text:
        if char.isdigit():
            result += char
            break
    return result


def total_calibration(cal_list):
    cal_values = []
    for item in cal_list:
        calibration = calibrate(item)
        cal_values.append(int(calibration))
    total = sum(cal_values)
    ic(cal_values)
    return total


map_valid_num(test_text_2)
# ic(total_calibration(valid_list))
