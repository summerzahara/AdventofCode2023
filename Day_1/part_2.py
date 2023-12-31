from icecream import ic

test_text_2 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234",
               "7pqrstsixteen"]

map_valid_nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}


# Open the file and convert to list of strings
def open_input_file():
    with open("day_1_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        return data


# Get the first number
def first(word):
    first_digit = []
    while True:
        if len(first_digit) > 0:
            break
        if word[0].isdigit():
            first_digit.append(word[0])
            break
        for key, value in map_valid_nums.items():
            if word.startswith(key):
                first_digit.append(value)
                break
        if word[0].isalpha():
            word = word[1:]
            continue
    return first_digit


# Get the last number
def last(word):
    last_digit = []
    while True:
        if len(last_digit) > 0:
            break
        if word[-1].isdigit():
            last_digit.append(word[-1])
            break
        for key, value in map_valid_nums.items():
            if word.endswith(key):
                last_digit.append(value)
                break
        if word[-1].isalpha():
            word = word[:-1]
            continue
    return last_digit


# Get calibrate num from first and last digits and out put the sum
def all_word(word_list):
    final_list = []
    for word in word_list:
        calibration = str(first(word)[0]) + str(last(word)[0])
        final_list.append(int(calibration))
    total = sum(final_list)
    return total


ic(all_word(open_input_file()))
