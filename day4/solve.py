input_filename = 'day4/input.txt'

with open(input_filename) as f:
    lines = f.readlines()

cards = [1] * len(lines)

for id, line in enumerate(lines):
    num_str = line.strip('\n').split(':')[1]
    win_str, have_str = num_str.split('|')

    matches = len(set(win_str.split()) & set(have_str.split()))

    for match in range(matches):
        cards[match+id+1] += cards[id]

print(sum(cards))