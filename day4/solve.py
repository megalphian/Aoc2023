input_filename = 'day4/input.txt'

with open(input_filename) as f:
    lines = f.readlines()

winnings = 0
multiplier_list = []

for id, line in enumerate(lines):
    num_str = line.strip('\n').split(':')[1]
    win_str, have_str = num_str.split('|')

    multiplier_list.append(id)
    multiplier = multiplier_list.count(id)

    matches = len(set(win_str.split()) & set(have_str.split()))

    for rep in range(multiplier):
        for match in range(matches):
            multiplier_list.append(id+1+match)
    winnings = winnings + multiplier

print(winnings)