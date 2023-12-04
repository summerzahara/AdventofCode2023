from icecream import ic
import re

test_data = ['467..114..', '...*......', '..35..633.', '......#...', '617*......', '.....+.58.', '..592.....', '......755.', '...$.*....', '.664.598..']


# Parse input file
def open_input_file():
    with open("d3_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        ic(data)

# open_input_file()

def analyze(input):
    master_list = []
    for line in input:
        line_list = []
        for char in line:
            if char == '.':
                line_list.append("n")
            elif char.isdigit():
                line_list.append(char)
            else:
                line_list.append("y")
        master_list.append(line_list)
    return master_list

# ic(analyze(test_data))

# Catalog Numbers
def catalog(list):
    master_catalog = []
    for item in list:
        row = list.index(item)
        number = ""
        i = []
        for x in item:
            if x.isdigit():
                number += x
                i.append(item.index(x))
            if x.isalpha():
                pass
        entry = row, number, i
        master_catalog.append(entry)
    return master_catalog

# ic(catalog(analyze(test_data)))

def test(list):
    dict = {}
    all_nums = []
    all_i = []
    for row in list:
        id = list.index(row)
        nums = re.findall(r'\d+', row)
        i_list = []
        for item in nums:
            i_start = row.index(item)
            i_end = i_start + len(item)-1
            i_list.append((i_start, i_end))
        dict[id] = nums, i_list
    return dict

ic(test(test_data))

def part_nums(master_list, dictionary):
    all_coords = []
    for item in master_list:
        for x in item:
            if x == 'y':
                coordinates = (master_list.index(item), item.index(x))
                all_coords.append(coordinates)
    ic(all_coords)
    total = []
    for item in all_coords:
        # Check all above
        if dictionary[item[0]][1]
        #  Check all below
        if master_list[item[0]+1][item[1]-1].isdigit():
            total.append(master_list[item[0]+1][item[1]-1])
        if master_list[item[0] + 1][item[1]].isdigit():
            total.append(master_list[item[0] + 1][item[1]])
        if master_list[item[0] + 1][item[1]+1].isdigit():
            total.append(master_list[item[0] + 1][item[1]+1])
        # Check row
        if master_list[item[0]][item[1]-1].isdigit():
            total.append(master_list[item[0]][item[1]-1])
        if master_list[item[0]][item[1]+1].isdigit():
            total.append(master_list[item[0]][item[1]+1])
    ic(total)
    total = [int(i) for i in total]
    ic(sum(total))


part_nums(analyze(test_data))

def tup_range(tuple):
    return list(range(tuple[0],tuple[1]+1))

item = (0,4)
ic(tup_range(item))
