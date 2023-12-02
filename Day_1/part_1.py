from icecream import ic

test_text = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

def open_input_file():
    with open("day_1_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        return data
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
    return total


if __name__ == '__main__':
    input_cal_values = open_input_file()
    ic(total_calibration(input_cal_values))
