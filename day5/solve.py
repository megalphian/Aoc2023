input_filename = 'day5/test.txt'

with open(input_filename) as f:
    lines = f.readlines()

import re

sec_num = 0
sections = [[],] * 8
sec_ref = ['seeds', 'seed_soil', 'soil_fert', 'fert_water', 'water_light', 'light_temp', 'temp_hum', 'hum_loc']

for line in lines:
    line = line.strip('\n')

    is_number = False
    is_number = re.search('\d', line)

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

for id, section in enumerate(sections):
    source_range, dest_range, range_len = 0, 1, 2
     
    for row in section:
        if id == 0:
            for seed in row:
                print(seed)
        
