input_file = open("./input.txt")
input_arr = []

for line in input_file:
    input_arr.append(line.strip().split(" "))

print(input_arr)

for i, line in enumerate(input_arr):
    print(line)
    for j, num in enumerate(line):
        line[j] = int(line[j]) 

    print(line)

    for k in range(25):
        j = 0
        while j < len(line):
            #print(f"j = {j} which is {line[j]}")
            if line[j] == 0:
                line[j] = 1
            elif len(str(line[j])) % 2 == 0:
                num_len = len(str(line[j]))
                #print(f"{str(line[j])[(int(num_len/2)):]} = {int(str(line[j])[(int(num_len/2)):])} and {str(line[j])[:int(num_len/2)]} = {int(str(line[j])[:int(num_len/2)])}")
                line.insert(j+1, int((str(line[j]))[int(num_len/2):])) 
                line[j] = int(str(line[j])[:int(num_len/2)])
                j += 1
                #print(f"j inc to {j}")
            else:
                line[j] = line[j] * 2024
            j += 1
        #print(line)
        print(len(line))

