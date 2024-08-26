engine = 'day3/input.txt'
with open(engine) as f:
    lines = f.readlines()
vals = []
sym_list = []
num_coor = []
confirm_list = []

number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dot = '.'

current_num = None
num_coor = []

for row in range(len(lines)):
    if current_num is not None:
        vals.append([current_num, num_coor])
        current_num = None
        num_coor = []
    for col in range(len(lines[row])-1):  
        char = lines[row][col]
        if char in number:
            if current_num is None:
                current_num = char
            elif current_num is not None:
                current_num = current_num + char
            num_coor.append([row,col])
        elif char == dot:
            if current_num is not None:
                vals.append([current_num, num_coor])
                current_num = None
                num_coor = []
        else:
            if current_num is not None:
                vals.append([current_num, num_coor])
                current_num = None
                num_coor = []
            sym_list.append([row,col])

for val, coords in vals:
    x_id = 0
    y_id = 1
    is_adj = False
    for num_id in range(len(coords)):
        for sym_id in range(len(sym_list)):
            if coords[num_id][x_id] == sym_list[sym_id][x_id]:
                if abs(coords[num_id][y_id] - sym_list[sym_id][y_id]) == 1:
                    is_adj = True
                    confirm_list.append(int(val))
            elif abs(coords[num_id][x_id] - sym_list[sym_id][x_id]) == 1:
                if coords[num_id][y_id] == sym_list[sym_id][y_id]:
                    is_adj = True
                    confirm_list.append(int(val))
                elif abs(coords[num_id][y_id] - sym_list[sym_id][y_id]) == 1:
                    is_adj = True
                    confirm_list.append(int(val))
            if is_adj:
                break
        if is_adj:
            break
# print(confirm_list)
print(sum(confirm_list))