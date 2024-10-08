input_filename = 'day5/test.txt'

with open(input_filename) as f:
    lines = f.readlines()

import re

def handle_overlap(seed_ranges):
    # Handle seed range overlap
    for i in range(len(seed_ranges)-1):
        for j in range(i+1, len(seed_ranges)):
            if(len(seed_ranges[i]) == 0 or len(seed_ranges[j]) == 0):
                continue
            a_1, b_1 = seed_ranges[i]
            a_2, b_2 = seed_ranges[j]
            if(a_2 > b_1):
                continue
            elif(b_1 >= a_2 and b_2 > b_1):
                seed_ranges[i] = [a_1, b_2]
                seed_ranges[j] = []
            elif(b_1 >= a_2 and b_2 <= b_1):
                seed_ranges[i] = [a_1, b_1]
                seed_ranges[j] = []

sec_num = 0
sections = [[],] * 8
sec_ref = ['seed_soil', 'soil_fert', 'fert_water', 'water_light', 'light_temp', 'temp_hum', 'hum_loc']

for line in lines:
    line = line.strip('\n')

    is_number = False
    is_number = re.search('[0-9]', line)

    if len(line) == 0:
        sec_num += 1
        sections[sec_num] = []
        continue
    
    if sec_num == 0:
        line = line.split(':')[1].strip().split()
        sections[sec_num] = [line]
    else:
        if is_number:
            line = line.split()
            sections[sec_num] += [line]

seed_list = sections[0][0]
maps = sections[1:]
seed_ranges = []

for i in range(len(seed_list)):
    if i % 2 == 0:
        seed_start = int(seed_list[i])
        length = int(seed_list[i+1])
        end = seed_start + length - 1
        seed_ranges += [[seed_start, end]]


# Handle overlap between seed ranges

# Sort the seed ranges by the start value
# seed_ranges = sorted(seed_ranges, key=lambda seed_range: seed_range[0])

# seed_ranges = [seed_range for seed_range in seed_ranges if len(seed_range) > 0]


# location = None
# ref_ranges = seed_ranges.copy()

# loop_length = len(sections[1:])
# counter = 0

# for section in sections[1:]:
#     new_ref_ranges = []
#     shifts = []
#     split_pairs = []
#     for dest, source, length in section:
#         # add split pairs to ref ranges and clear split pairs
#         ref_ranges += split_pairs
#         split_pairs = []

#         min = int(source)
#         max = int(source) + int(length)
#         shift = int(dest) - int(source)

#         for ref_range in ref_ranges:
#             a, b = ref_range
#             transform_pair = None
#             new_split_pairs = []
#             # There is overlap between the map and the ranges we have
#             if(min >= a and min <= b):
#                 if(max <= b):
#                     transform_pair = [min, max]
#                     new_split_pairs = [[a, min-1], [max+1, b]]
#                 else:
#                     transform_pair = [min, b]
#                     new_split_pairs = [[a, min-1]]
#             elif(max >= a and max <= b):
#                 # recall min is not within the range
#                 transform_pair = [a, max]
#                 new_split_pairs = [[max + 1, b]]    
            
#             if transform_pair:
#                 new_ref_ranges.append(transform_pair)
#                 shifts.append(shift)

#             new_split_pairs = [split_pair for split_pair in new_split_pairs if split_pair[0] <= split_pair[1]]
#             split_pairs += new_split_pairs
#     ref_ranges += split_pairs
#     split_pairs = []

#     for i in range(len(new_ref_ranges)):
#         new_range = new_ref_ranges[i]
#         shift = shifts[i]
#         ref_ranges += [[a + shift for a in new_range]]

#     handle_overlap(ref_ranges)
#     ref_ranges = [ref_range for ref_range in ref_ranges if len(ref_range) > 0]

#     counter += 1
#     print('Done section '+ str(counter) + ' out of ' + str(loop_length))

# for a, b in ref_ranges:
#     if location is None:
#         location = a
#     elif location > a:
#         location = a

# print(location)

current_ranges = []
location_ranges = []

for i, section in enumerate(maps):
    for dest, source, length in section:
        map_start = int(source)
        map_end = int(source) + int(length) - 1
        shift = int(dest) - int(source)
        next_unsplit = []
        print(sec_ref[i])

        for seed_start, seed_end in seed_ranges:
            print(seed_start, seed_end)
            print(map_start, map_end)
            if seed_start <= map_start <= seed_end:
                split_start = map_start
            elif map_start <= seed_start <= map_end:
                split_start = seed_start
            else:
                next_unsplit += [(seed_start, seed_end)]
                continue

            if seed_start <= map_end <= seed_end:
                split_end = map_end
            elif map_start <= seed_end <= map_end:
                split_end = seed_end
            else:
                next_unsplit += [(seed_start, seed_end)]
                continue
            
            current_ranges += [(split_start + shift,  split_end + shift)]

            if split_start > seed_start:
                next_unsplit += [(seed_start, split_start - 1)]
            if split_end < seed_end:
                next_unsplit += [(split_end + 1, seed_end)]
    print(current_ranges)

print(location_ranges)

