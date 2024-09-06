input_filename = "day6/input.txt"

with open(input_filename) as f:
    lines = f.readlines()

time_vals = lines[0].strip('\n').split(':')[1].split()

dist_vals = lines[1].strip('\n').split(':')[1].split()

total_count = []

for i in range(len(time_vals)):
    count = 0
    time = int(time_vals[i])
    dist = int(dist_vals[i])
    for hold_time in range(time + 1):
        if (hold_time * (time - hold_time)) > dist:
            count += 1
    total_count += [count]

product = 1
for x in total_count:
    product *= x

print(product)