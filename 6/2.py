input_file = open("./eg-input.txt")
f = open("./debug-path.txt", "w")
input_arr = []

for line in input_file:
    input_arr.append(line.strip())

#print(input_arr)

current_i, current_j = -1, -1

# find current position
for i, inp in enumerate(input_arr):
    for j, ch in enumerate(inp):
        if input_arr[i][j] == '^':
            current_i = i
            current_j = j 
            break
    if current_i != -1:
        break

first_i, first_j = current_i, current_j
first_dir = "U"
current_direction = first_dir

infinite_loop_count = 0


# keep going in current direction until obstacle encountered or out of range
# out_of_maze_condition = going up and i == 0 or going down and i == len(input_arr) or going left and j == 0 or going right and j == len(input_arr[i])
# obstacle condition = arr[i][j] == '#'

#print(len(input_arr)-1)
#print(len(input_arr[0])-1)

# find current position
for i, inp in enumerate(input_arr):
    for j, ch in enumerate(inp):
        f.write(f"i,j: {i},{j}\n")
        if input_arr[i][j] == '#' or (i == first_i and j == first_j):   # can't put obstacle in first position
            continue
        else:
            current_direction = first_dir
            current_i = first_i
            current_j = first_j
            
            tmp = input_arr[:]
            tmp[i] = tmp[i][:j] + '#' + tmp[i][j+1:]    # add obstacle
            tmp[current_i] = tmp[current_i][:current_j] + 'X' + tmp[current_i][current_j+1:]    # mark X for starting position

            dir_arr = tmp[:]
            dir_arr[current_i] = dir_arr[current_i][:current_j] + current_direction + dir_arr[current_i][current_j+1:]    # mark direction

            for line in dir_arr:
                f.write(f"{line}\n")
            
            f.write(f"\n")
            
            for line in tmp:
                f.write(f"{line}\n")

            # go through maze
            while not (current_i == 0 or current_i == len(tmp)-1 or current_j == 0 or current_j == len(tmp[0])-1):
                #print(f"{current_i}, {current_j} in {current_direction}")
                f.write(f"{current_i}, {current_j} in {current_direction}\n")
                if current_direction == "U":
                    if tmp[current_i-1][current_j] == '#': #obstacle
                        #print(f"obstacle in {current_i-1}, {current_j}\n")
                        f.write(f"obstacle in {current_i-1}, {current_j}\n")
                        current_direction = "R"
                    else:
                        current_i -= 1
                        if tmp[current_i][current_j] != 'X':
                            tmp[current_i] = tmp[current_i][:current_j] + 'X' + tmp[current_i][current_j+1:]
                            dir_arr[current_i] = dir_arr[current_i][:current_j] + current_direction + dir_arr[current_i][current_j+1:]
                        elif dir_arr[current_i][current_j] == current_direction:  #infinite loop
                            infinite_loop_count += 1
                            f.write(f"infinite loop in {i},{j}")
                            break
                elif current_direction == "D":
                    if tmp[current_i+1][current_j] == '#': #obstacle
                        #print(f"obstacle in {current_i+1}, {current_j}\n")
                        f.write(f"obstacle in {current_i+1}, {current_j}\n")
                        current_direction = "L"
                    else:
                        current_i += 1
                        if tmp[current_i][current_j] != 'X':
                            tmp[current_i] = tmp[current_i][:current_j] + 'X' + tmp[current_i][current_j+1:]
                            dir_arr[current_i] = dir_arr[current_i][:current_j] + current_direction + dir_arr[current_i][current_j+1:]
                        elif dir_arr[current_i][current_j] == current_direction:  #infinite loop
                            infinite_loop_count += 1
                            f.write(f"infinite loop in {i},{j}")
                            break
                            
                elif current_direction == "L":
                    if tmp[current_i][current_j-1] == '#': #obstacle
                        #print(f"obstacle in {current_i}, {current_j-1}\n")
                        f.write(f"obstacle in {current_i}, {current_j-1}\n")
                        current_direction = "U"
                    else:
                        current_j -= 1
                        if tmp[current_i][current_j] != 'X':
                            tmp[current_i] = tmp[current_i][:current_j] + 'X' + tmp[current_i][current_j+1:]
                            dir_arr[current_i] = dir_arr[current_i][:current_j] + current_direction + dir_arr[current_i][current_j+1:]
                        elif dir_arr[current_i][current_j] == current_direction:  #infinite loop
                            infinite_loop_count += 1
                            f.write(f"infinite loop in {i},{j}")
                            break
                            
                else:
                    if tmp[current_i][current_j+1] == '#': #obstacle
                        #print(f"obstacle in {current_i}, {current_j+1}\n")
                        f.write(f"obstacle in {current_i}, {current_j+1}\n")
                        current_direction = "D"
                    else:
                        current_j += 1
                        if tmp[current_i][current_j] != 'X':
                            tmp[current_i] = tmp[current_i][:current_j] + 'X' + tmp[current_i][current_j+1:]
                            dir_arr[current_i] = dir_arr[current_i][:current_j] + current_direction + dir_arr[current_i][current_j+1:]
                        elif dir_arr[current_i][current_j] == current_direction:  #infinite loop
                            infinite_loop_count += 1
                            f.write(f"infinite loop in {i},{j}")
                            break
                            
                f.write(f"{infinite_loop_count}\n")

                #print(path_count)

            for line in dir_arr:
                f.write(f"{line}\n")

            f.write(f"\n")

print(infinite_loop_count)

