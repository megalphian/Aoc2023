input_filename = 'input.txt'

with open(input_filename) as f:
    lines = f.readlines()

all_games = []

for line in lines:
    game_list = []
    game_str, input_str = line.strip('\n').split(':')
    game_sets = input_str.split(';')

    for set in game_sets:
        cube_groups = set.split(',')
        game_list.append(cube_groups)
    
    all_games.append(game_list)

power_list = []

for i in range(len(all_games)):
    game = all_games[i]
    is_valid = True
    red = 0
    green = 0
    blue = 0
    for cube_groups in game:
        for group in cube_groups:
            number, colour = group.strip(' ').split(' ')
            number = int(number)
            if colour == 'red' and number > red:
                red = number               
            elif colour == 'green' and number > green:
                green = number
            elif colour == 'blue' and number > blue:
                blue = number
    power_list.append(red * green * blue)
print(sum(power_list))
