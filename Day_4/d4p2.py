from icecream import ic


def open_input_file():
    with open("d4_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        my_data = []
        for string in data:
            string = string.split(":")
            string[0] = " ".join(string[0].split())
            my_data.append(string)
        for entry in my_data:
            entry[1] = entry[1].split("|")
        # ic(my_data)
        return my_data


input = open_input_file()


def compare_nums(list):
    copy_dict = {}
    for item in list:
        l1 = item[1][0].split()
        l2 = item[1][1].split()
        winners = []
        for num in l1:
            if num in l2:
                winners.append(num)
        copies = len(winners)
        copy_dict[item[0]] = copies
    return copy_dict


copies = compare_nums(input)


def count_cards(master_dict):
    count_dict = {}
    # Set initial card count to 1
    for i in range(1, len(master_dict) + 1):
        count_dict[i] = 1
    # Loop through all cards
    for i in range(1, len(master_dict) + 1):
        copy = master_dict[f"Card {i}"]
        # Check how many times we add copies
        for n in range(1, count_dict[i] + 1):
            # Add card for each copy
            for c in range(1, copy + 1):
                count_dict[i + c] += 1
    ic(count_dict)
    ic(sum(count_dict.values()))


count_cards(copies)
