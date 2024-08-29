input_filename = 'day5/input.txt'

with open(input_filename) as f:
    lines = f.readlines()

import re

sec_num = 0
sections = [[],] * 8
sec_ref = ['seeds', 'seed_soil', 'soil_fert', 'fert_water', 'water_light', 'light_temp', 'temp_hum', 'hum_loc']

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
location = None

for seed in seed_list:
    ref_number = int(seed)

    for id, section in enumerate(sections[1:]):
        for dest, source, len in section:
            min = int(source)
            max = int(source) + int(len)
            shift = int(dest) - int(source)

            if ref_number >= min and ref_number <= max:
                ref_number += shift
                break   

    if location is None:
        location = ref_number
    elif location > ref_number:
        location = ref_number            

print(location)
        
