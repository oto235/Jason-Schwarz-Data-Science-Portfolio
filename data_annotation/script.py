# Below is a Python function that decodes a text file into a message using a pyramid structure. First, it initializes needed variables. Then, after opening the text file, it iterates 
# through each line adding it to a dictionary. Next, it creates a sorted list needed to feed into a while loop to create the pyramid structure. The while loop gracefully handles the 
# edge case of not having the 'correct' number of items to build a 'perfect' pyramid; however, it still creates a pyramid. Lastly, a for loop uses the last number in each pyramid row to 
# extract the matched word from the dictionary to build the final message, which is returned. Note, the function returns an empty string if the text file is empty.


def decode(message_file): 
    # init
    line_dict = dict()
    num_list = list()
    step = 1
    subsets = [] 
    message = ""

    # iterate through text file
    with open(message_file, 'r') as text_file:
        for line in text_file:
            line = line.lstrip().rstrip('\n')  # remove leading space if any and 'newline' 
            line_split = line.split(' ', 1)  # split by first space after number
            line_dict.setdefault(line_split[0], line_split[1])  # add number and word(s) to dictionary
    text_file.close()
    
    # set up list for pyramid
    num_list = sorted(list(line_dict.keys()))
    
    # create pyramid within 'subsets'
    while len(num_list) != 0:
        if len(num_list) >= step:
            subsets.append(num_list[0:step])
            num_list = num_list[step:]
            step += 1
        else:
            print("WARNING: Last line does not have the correct number of items to make a valid pyramid.")
            break

    # build message from pyramid 
    for set in subsets:
        last_num = set[-1]
        last_word = line_dict[last_num]
        message += last_word + ' '

    # return desirable
    return message[:-1].lower()

if __name__ == "__main__":
    filepath = 'data_annotation/coding_qual_input.txt'
    message = decode(filepath)
    print(message)
    