file = 'data_annotation/messfile.txt'

with open(file, 'r') as text_file:
    line_dict = dict()
    num_list = list()
    for line in text_file:
        line = line.lstrip()  # remove leading space if any
        line_split = line.split(' ', 1)  # split by first space after number
        line_dict.setdefault(line_split[0], line_split[1])
        num_list.append(line_split[0])
    num_list = sorted(num_list)
text_file.close()

def create_pyramid(nums):
    step = 1
    subsets = []
    while len(nums) != 0:
        if len(nums) >= step:
            subsets.append(nums[0:step])
            nums = nums[step:]
            step += 1
        else:
            return False
            
    return subsets
    
pyramid = create_pyramid(num_list)
print(pyramid)
for set in pyramid:
    last_num = set[-1]
    last_word = line_dict[last_num]
    print(last_word)

def decode(message_file): 
    pass