engine = 'day3/input.txt'
with open(engine) as f:
    lines = f.readlines()
vals = []
gear_list = []
num_coor = []
confirm_list = []

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
gear = '*'

current_num = ''
num_coor = []

for row in range(len(lines)):
    if len(current_num) > 0:
        vals.append([current_num, num_coor])
        current_num = ''
        num_coor = []
    for col in range(len(lines[row])-1):  
        char = lines[row][col]
        if char in number:
            current_num = current_num + char
            num_coor.append([row,col])
        else:
            if len(current_num) > 0:
                vals.append([current_num, num_coor])
                current_num = ''
                num_coor = []

            if char == gear:
                gear_list.append([row,col])

for gear_id in range(len(gear_list)):
    for val, coords in vals:
        x_id = 0
        y_id = 1
        is_adj = False
        for num_id in range(len(coords)):
            if (abs(coords[num_id][x_id] - gear_list[gear_id][x_id]) <= 1 and abs(coords[num_id][y_id] - gear_list[gear_id][y_id]) <= 1):
                is_adj = True
                confirm_list.append([gear_list[gear_id], val])
            if is_adj:
                break
product_list = []

for h in range(len(confirm_list)):
    counter = 0
    if confirm_list[h][0] == confirm_list[h-1][0]:
        product_list.append(int(confirm_list[h][1])*int(confirm_list[h-1][1]))

print(sum(product_list))