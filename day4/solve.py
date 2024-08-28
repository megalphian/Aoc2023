input_filename = 'day4/input.txt'

with open(input_filename) as f:
    lines = f.readlines()

winnings = 0
number = ['0','1','2','3','4','5','6','7','8','9']

for line in lines:
    num_str = line.strip('\n').split(':')[1]
    win_str, have_str = num_str.split('|')

    count = len(set(win_str.split()) & set(have_str.split()))
    if count > 0:
        winnings += 2 ** (count - 1)

print(winnings)