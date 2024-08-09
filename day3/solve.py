engine = 'input.txt'
with open(engine) as f:
    lines = f.readlines()
vals = []
row_nums = []
col_nums = []
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dot = '.'
for row in range(len(lines)):
    current_num = None
    for col in range(len(lines[row])):
       if lines[row][col] in number:
           num_char = lines[row][col]
           pass
