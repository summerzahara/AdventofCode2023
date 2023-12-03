from icecream import ic

test_text = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]


# Open the file and convert to list of strings
def open_input_file():
    with open("day_1_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        return data

# Pull first and list number from each and output new "calibration"
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

# Total all values
def total_calibration(cal_list):
    cal_values = []
    for item in cal_list:
        calibration = calibrate(item)
        cal_values.append(int(calibration))
    total = sum(cal_values)
    ic(cal_values)
    return total

# ic(total_calibration(open_input_file()))
