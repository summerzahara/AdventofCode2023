from icecream import ic

colors = ['red', 'green', 'blue']

# Open the file and convert to list of strings
def open_input_file():
    with open("day2_input.txt", "r") as file:
        data = [item.strip() for item in file.readlines()]
        my_data = []
        for string in data:
            string = string.split(";")
            my_data.append(string)
        return my_data


test_input = [['Game 1: 3 blue, 4 red', '1 red, 2 green, 6 blue', '2 green'],
['Game 2: 1 blue, 2 green',' 3 green, 4 blue, 1 red', '1 green, 1 blue'],
['Game 3: 8 green, 6 blue, 20 red', '5 blue, 4 red, 13 green', '5 green, 1 red'],
['Game 4: 1 green, 3 red, 6 blue', '3 green, 6 red', '3 green, 15 blue, 14 red'],
['Game 5: 6 red, 1 blue, 3 green', '2 blue, 1 red, 2 green']]
my_input = open_input_file()

def id_game(full_list):
    game = full_list[0]
    for i in game.split():
        if ":" in i:
            game_id = i[:-1]
    return game_id


def find_digit(string):
    digits = ""
    for char in string:
        if char.isdigit():
            digits += char
    return int(digits)



"12 red cubes, 13 green cubes, and 14 blue cubes"
def count_colors(full_list):
    possible = True
    # ic(full_list[0])
    i = full_list[0].index(":")
    full_list[0] = full_list[0][i+1:]
    # ic(full_list)
    for item in full_list:
        for x in item.split(","):
            count = find_digit(x)
            if "green" in x:
                if count > 13:
                    possible = False
            elif "red" in x:
                if count > 12:
                    possible = False
            elif "blue" in x:
                if count > 14:
                    possible = False
    return possible

possible_games = []
for entry in my_input:
    game = int(id_game(entry))
    if count_colors(entry):
        possible_games.append(game)
ic(possible_games)
ic(sum(possible_games))



