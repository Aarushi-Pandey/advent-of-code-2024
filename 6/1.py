input_file = open("./input.txt")
f = open("./debug-path.txt", "w")
input_arr = []

for line in input_file:
    input_arr.append(line.strip())

#print(input_arr)

current_i, current_j = -1, -1
current_direction = "up"

# find current position
for i, inp in enumerate(input_arr):
    for j, ch in enumerate(inp):
        if input_arr[i][j] == '^':
            current_i = i
            current_j = j 
            break
    if current_i != -1:
        break

path_count = 1

# keep going in current direction until obstacle encountered or out of range
# out_of_maze_condition = going up and i == 0 or going down and i == len(input_arr) or going left and j == 0 or going right and j == len(input_arr[i])
# obstacle condition = arr[i][j] == '#'

print(len(input_arr)-1)
print(len(input_arr[0])-1)

input_arr[current_i] = input_arr[current_i][:current_j] + 'X' + input_arr[current_i][current_j+1:]


while not (current_i == 0 or current_i == len(input_arr)-1 or current_j == 0 or current_j == len(input_arr[0])-1):
    #print(f"{current_i}, {current_j} in {current_direction}")
    f.write(f"{current_i}, {current_j} in {current_direction}\n")
    if current_direction == "up":
        if input_arr[current_i-1][current_j] == '#': #obstacle
            #print(f"obstacle in {current_i-1}, {current_j}\n")
            f.write(f"obstacle in {current_i-1}, {current_j}\n")
            current_direction = "right"
        else:
            current_i -= 1
            if input_arr[current_i][current_j] != 'X':
                input_arr[current_i] = input_arr[current_i][:current_j] + 'X' + input_arr[current_i][current_j+1:]
                path_count += 1
    elif current_direction == "down":
        if input_arr[current_i+1][current_j] == '#': #obstacle
            #print(f"obstacle in {current_i+1}, {current_j}\n")
            f.write(f"obstacle in {current_i+1}, {current_j}\n")
            current_direction = "left"
        else:
            current_i += 1
            if input_arr[current_i][current_j] != 'X':
                input_arr[current_i] = input_arr[current_i][:current_j] + 'X' + input_arr[current_i][current_j+1:]
                path_count += 1
    elif current_direction == "left":
        if input_arr[current_i][current_j-1] == '#': #obstacle
            #print(f"obstacle in {current_i}, {current_j-1}\n")
            f.write(f"obstacle in {current_i}, {current_j-1}\n")
            current_direction = "up"
        else:
            current_j -= 1
            if input_arr[current_i][current_j] != 'X':
                input_arr[current_i] = input_arr[current_i][:current_j] + 'X' + input_arr[current_i][current_j+1:]
                path_count += 1
    else:
        if input_arr[current_i][current_j+1] == '#': #obstacle
            #print(f"obstacle in {current_i}, {current_j+1}\n")
            f.write(f"obstacle in {current_i}, {current_j+1}\n")
            current_direction = "down"
        else:
            current_j += 1
            if input_arr[current_i][current_j] != 'X':
                input_arr[current_i] = input_arr[current_i][:current_j] + 'X' + input_arr[current_i][current_j+1:]
                path_count += 1
    f.write(f"{path_count}\n")
    #print(path_count)

for line in input_arr:
    f.write(f"{line}\n")

print(path_count)

