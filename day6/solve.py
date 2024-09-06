input_filename = "day6/input.txt"

with open(input_filename) as f:
    lines = f.readlines()

time_vals = lines[0].strip('\n').split(':')[1].replace(" ", '')

dist_vals = lines[1].strip('\n').split(':')[1].replace(" ", "")

count = 0
time = int(time_vals)
dist = int(dist_vals)

for hold_time in range(time + 1):
    if (hold_time * (time - hold_time)) > dist:
        count += 1

print(count)