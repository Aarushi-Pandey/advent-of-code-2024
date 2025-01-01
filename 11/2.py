import copy

input_file = open("./input.txt")
input_arr = []

for line in input_file:
    input_arr.append(line.strip().split(" "))

print(input_arr)

for i, line in enumerate(input_arr):
    print(line)

    line_dict = {}
    for j, num in enumerate(line):
        line[j] = int(line[j])
        if int(line[j]) in line_dict:
            line_dict[int(line[j])] += 1
        else:
            line_dict[int(line[j])] = 1 

    print(line)

    for k in range(75):
        new_line_dict = {}
        for key in line_dict:
            #print(f"j = {j} which is {line[j]}")
            if key == 0:
                if 1 in new_line_dict:
                    new_line_dict[1] += line_dict[key]
                else:
                    new_line_dict[1] = line_dict[key]
                #line_dict[key] = 0
            elif len(str(key)) % 2 == 0:
                num_len = len(str(key))
                #print(f"{str(line[j])[(int(num_len/2)):]} = {int(str(line[j])[(int(num_len/2)):])} and {str(line[j])[:int(num_len/2)]} = {int(str(line[j])[:int(num_len/2)])}")
                if int((str(key))[int(num_len/2):]) in new_line_dict:
                    new_line_dict[int((str(key))[int(num_len/2):])] += line_dict[key]
                else:
                    new_line_dict[int((str(key))[int(num_len/2):])] = line_dict[key]

                if int(str(key)[:int(num_len/2)]) in new_line_dict:
                    new_line_dict[int(str(key)[:int(num_len/2)])] += line_dict[key]
                else:
                    new_line_dict[int(str(key)[:int(num_len/2)])] = line_dict[key]
                #line_dict[key] = 0
                #print(f"j inc to {j}")
            else:
                if key*2024 in new_line_dict:
                    new_line_dict[key * 2024] += line_dict[key]
                else:
                    new_line_dict[key * 2024] = line_dict[key]
                #line_dict[key] = 0
        #print(line)
        line_dict = copy.deepcopy(new_line_dict)
        len_line_dict = 0
        for key in line_dict:
            len_line_dict += line_dict[key]
        # print(line_dict)
        print(len_line_dict)

