from icecream import ic
map_valid_nums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
test_word = "onesevenvchtfkbfkgzrhzhpsg3six"
test_2 = "6six26gkj2"
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
            ic(word)
            continue
    ic(first_digit)
    return first_digit

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
            ic(word)
            continue
    ic(last_digit)
    return last_digit

calibration = str(first(test_2)[0]) + str(last(test_2)[0])
ic(calibration)
