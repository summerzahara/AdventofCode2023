from icecream import ic


def open_input_file():
    with open("d4_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        my_data = []
        for string in data:
            string = string.split(":")
            my_data.append(string)
        for entry in my_data:
            entry[1] = entry[1].split("|")
        return my_data


input = open_input_file()

def compare_nums(list):
    all_winners = []
    for item in list:
        l1 = item[1][0].split()
        l2 = item[1][1].split()
        # ic(item[1])
        # ic(l1,l2)
        winners = []
        for num in l1:
            if num in l2:
                winners.append(num)

        if len(winners) == 0:
            pass
        elif len(winners) == 1:
            points = 1
            all_winners.append(points)
        else:
            points = 1
            for n in range(len(winners) - 1):
                points = points * 2
            all_winners.append(points)
    ic(all_winners)
    ic(sum(all_winners))


compare_nums(input)
