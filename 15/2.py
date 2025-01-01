input_file = open("./eg3-input.txt")
position_arr = []
moves = []

for line in input_file:
    if '#' not in line:
        if '<' not in line and '>' not in line and '^' not in line and 'v' not in line:
            continue
        else:
            moves = line.strip()
    else:
        position_arr.append(line.strip().replace(".","..").replace("O", "[]").replace("#","##").replace("@","@."))

print(position_arr)
print(moves)

position = [-1, -1]

# find current position
for i, line in enumerate(position_arr):
    for j, ch in enumerate(line):
        if ch == '@':
            position = [i, j]
            break

# start moving
for i, move in enumerate(moves):
    new_i, new_j = position[0], position[1]

    if move == '>':
        new_j += 1
    elif move == '<':
        new_j -= 1
    elif move == '^':
        new_i -= 1
    else:
        new_i += 1

    print(move)
    
    new_position = position_arr[new_i][new_j]
    if new_position == '#':
        # can't move since end, do nothing
        print("border")
    elif new_position == '[' or new_position == ']':
        # check if obstacle can be moved
        print("obstacle")
        obstacle_i, obstacle_j = new_i, new_j
        if move == '>':
            while (position_arr[obstacle_i][obstacle_j] == '[' or position_arr[obstacle_i][obstacle_j] == ']') and position_arr[obstacle_i][obstacle_j] != '#':
                if position_arr[obstacle_i][obstacle_j] == '.':
                    break
                obstacle_j += 1
            
            if position_arr[obstacle_i][obstacle_j] == '.':
                print("able to move even with obstacle")
                position_arr[obstacle_i] = position_arr[obstacle_i][:obstacle_j] + position_arr[obstacle_i][obstacle_j+1:new_j] + '@' + position_arr[obstacle_i][new_j+1:]

                # removing @ from original position
                position_arr[position[0]] = position_arr[position[0]][:position[1]] + '.' + position_arr[position[0]][position[1]+1:]
                
                position = [new_i, new_j]
            else:
                print("cant move due to obstacle")

        elif move == '<':
            while (position_arr[obstacle_i][obstacle_j] == '[' or position_arr[obstacle_i][obstacle_j] == ']') and position_arr[obstacle_i][obstacle_j] != '#':
                if position_arr[obstacle_i][obstacle_j] == '.':
                    break
                obstacle_j -= 1

            if position_arr[obstacle_i][obstacle_j] == '.':
                print("able to move even with obstacle")
                position_arr[obstacle_i] = position_arr[obstacle_i][:obstacle_j] + position_arr[obstacle_i][obstacle_j+1:new_j] + '@' + position_arr[obstacle_i][new_j+1:]

                # removing @ from original position
                position_arr[position[0]] = position_arr[position[0]][:position[1]] + '.' + position_arr[position[0]][position[1]+1:]
                
                position = [new_i, new_j]
            else:
                print("cant move due to obstacle")

        elif move == '^':
            # need to fix this so that it checks all oobstacles impacted, not just those directly above it
            if position_arr[obstacle_i][obstacle_j]
            while (position_arr[obstacle_i][obstacle_j] == '[' or position_arr[obstacle_i][obstacle_j] == ']') and position_arr[obstacle_i][obstacle_j] != '#':
                if position_arr[obstacle_i][obstacle_j] == '.' and position_arr[obstacle_i][obstacle_j] == '.':
                    break
                obstacle_i -= 1

            if position_arr[obstacle_i][obstacle_j] == '.':
                print("able to move even with obstacle")
                position_arr[obstacle_i] = position_arr[obstacle_i][:obstacle_j] + position_arr[obstacle_i][obstacle_j+1:new_j] + '@' + position_arr[obstacle_i][new_j+1:]

                # removing @ from original position
                position_arr[position[0]] = position_arr[position[0]][:position[1]] + '.' + position_arr[position[0]][position[1]+1:]
                
                position = [new_i, new_j]
            else:
                print("cant move due to obstacle")

        else:
            while (position_arr[obstacle_i][obstacle_j] == '[' or position_arr[obstacle_i][obstacle_j] == ']') and position_arr[obstacle_i][obstacle_j] != '#':
                if position_arr[obstacle_i][obstacle_j] == '.':
                    break
                obstacle_i += 1
    else:
        # open position
        print("easy move")
        position_arr[new_i] = position_arr[new_i][:new_j] + '@' + position_arr[new_i][new_j+1:]
        position_arr[position[0]] = position_arr[position[0]][:position[1]] + '.' + position_arr[position[0]][position[1]+1:]
        position = [new_i, new_j]
    
    print(position_arr)


print(position_arr)

# coordinate_sum = 0

# # find coordinate sum
# for i, line in enumerate(position_arr):
#     for j, ch in enumerate(line):
#         if ch == 'O':
#             coordinate_sum += 100 * i + j 

# print(coordinate_sum)