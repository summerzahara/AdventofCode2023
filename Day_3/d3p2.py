from icecream import ic

def open_input_file():
    with open("d3_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
    return data


def analyze(input):
    master_list = []
    for line in input:
        line_list = []
        for char in line:
            if char == '.':
                line_list.append("n")
            elif char.isdigit():
                line_list.append(char)
            elif char == '*':
                line_list.append(char)
            else:
                line_list.append("y")
        master_list.append(line_list)
    # ic(master_list)
    return master_list

# ic(analyze(open_input_file()))

# Parse data to create a dictionary row: [all numbers] [ (start index, end index)]
def create_index_dict(list):
    all_dict = {}
    for row in list:
        id = list.index(row)
        start_index = 0
        while start_index < len(row):
            end_index = start_index
            while end_index < len(row) and row[end_index].isdigit():
                end_index += 1
            if start_index != end_index:
                number = row[start_index:end_index]
                if id in all_dict.keys():
                    all_dict[id][0].append(number)
                    all_dict[id][1].append((start_index, end_index - 1))
                else:
                    all_dict[id] = ([number],[])
                    all_dict[id][1].append((start_index, end_index - 1))
            start_index = end_index + 1
    # ic(all_dict)
    return all_dict

def tup_range(tuple):
    return list(range(tuple[0], tuple[1] + 1))

def gear_ratio(master_list, dictionary):
    # Get coordinates where there are 'symbols'
    all_coords = []
    for item in master_list:
        item_size = len(item)
        for i in range(item_size):
            if item[i] == '*':
                coord = (master_list.index(item), i)
                all_coords.append(coord)
    # ic(all_coords)
    total_dict = {}
    total_ratios = []
    # check for numbers touching symbols
    for item in all_coords:
        item_nums = []
        row_num = item[0]
        # row above
        if row_num == 0:
            pass
        elif row_num - 1 in dictionary.keys():
            row_above = dictionary[row_num - 1]
            for entry in row_above[1]:
                index = tup_range(entry)
                if (item[1] - 1) in index or item[1] in index or (item[1] + 1) in index:
                    entry_index = row_above[1].index(entry)
                    num = row_above[0][entry_index]
                    item_nums.append(num)

        # same row
        if row_num in dictionary.keys():
            row = dictionary[row_num]
            for entry in row[1]:
                index = tup_range(entry)
                if (item[1] - 1) in index or (item[1] + 1) in index:
                    entry_index = row[1].index(entry)
                    num = row[0][entry_index]
                    item_nums.append(num)
        # row below
        if row_num + 1 in dictionary.keys():
            row_below = dictionary[row_num + 1]
            for entry in row_below[1]:
                index = tup_range(entry)
                if (item[1] - 1) in index or item[1] in index or (item[1] + 1) in index:
                    entry_index = row_below[1].index(entry)
                    num = row_below[0][entry_index]
                    item_nums.append(num)
        if len(item_nums) == 2:
            # ic(item_nums)
            ratio = 1
            for i in item_nums:
                ratio *= int(i)
            total_ratios.append(ratio)
    # ic(total_dict)
    # ic(total_ratios)
    sum_total = sum(total_ratios)
    ic(sum_total)

gear_ratio(analyze(open_input_file()), create_index_dict(open_input_file()))