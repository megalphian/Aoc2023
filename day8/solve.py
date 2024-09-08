filename = 'day8/input.txt'

from itertools import cycle
import re
import math

with open(filename) as f:
    lines = f.readlines()

raw_directions = lines[0].strip('\n')
directions = cycle(raw_directions)
locations = []
set_starts = []

for line in lines[2:]:
    location_in, location_out = line.strip('\n').split('=')
    location_in = location_in.strip()

    left_out, right_out = location_out.strip().strip('(').strip(')').split(',')
    right_out = right_out.strip()

    locations += [[location_in, left_out, right_out]]
    set_starts += re.findall('..A', location_in)

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
    count = 0
    for i, direction in enumerate(directions):
        location = find_location(location, direction)
        if re.search('..Z', location):
            if count == 0:
                i1 = i+1
            elif count == 1:
                i2 = i+1
            elif count == 2:
                i3 = i+1
                return(i3-i2)
                break
            count += 1
        if i == 100000:
            break


set_ends = []
for start in set_starts:
    set_ends += [repeating_search(start)]

print(math.lcm(*set_ends))
