input_filename = 'input.txt'

with open(input_filename) as f:
    lines = f.readlines()

def assign_numbers(first_number, num_char):
    # Return first_number and last_number in that order
    if first_number is None:
        return num_char, num_char
    else:
        return first_number, num_char

codes = []
numbers = ['0','1','2','3','4','5','6','7','8','9']
number_texts = ['zero','one','two','three','four','five','six','seven','eight','nine']
word_lengths = [3,4,5]
for line in lines:
    first_number = None
    last_number = None

    for i in range(len(line)):
        num_char = line[i]
        if num_char in numbers:
            first_number, last_number = assign_numbers(first_number, num_char)

        for offset in word_lengths:
            if i+offset <= len(line):
                sub_str = line[i:i+offset]
                if sub_str in number_texts:
                    # Assign first and last numbers
                    num_char = str(number_texts.index(sub_str))
                    first_number, last_number = assign_numbers(first_number, num_char)

    line_code = int(first_number + last_number)
    codes.append(line_code)

print(sum(codes))