filename = 'day8/input.txt'

from itertools import cycle

with open(filename) as f:
    lines = f.readlines()

raw_directions = lines[0].strip('\n')
directions = cycle(raw_directions)
locations = []

for line in lines[2:]:
    location_in, location_out = line.strip('\n').split('=')
    location_in = location_in.strip()

    left_out, right_out = location_out.strip().strip('(').strip(')').split(',')
    right_out = right_out.strip()

    locations += [[location_in, left_out, right_out]]

location = 'AAA'
location_out = 0

def find_location(location_in, direction):
    for start_loc, left_loc, right_loc in locations:
        if start_loc == location_in:
            if direction == 'L':
                location_out = left_loc
                break
            if direction == 'R':
                location_out = right_loc
                break
    return(location_out)

def repeating_search(location):
    for i, direction in enumerate(directions):
        location = find_location(location, direction)
        if location == 'ZZZ':
            print('missed me hehe')
            break
        if i == 1000000:
            break
    print(i+1)

repeating_search(location)


