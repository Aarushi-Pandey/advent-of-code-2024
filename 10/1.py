input_file = open("./input.txt")
input_arr = []

for line in input_file:
    input_arr.append(line.strip())

print(f"row length: {len(input_arr)}")
print(f"col length: {len(input_arr[0])}")

def recur_find_all_paths(i, j, input_arr, nine_arr, goal):
    #print(f"{i},{j}")
    if i < 0 or i == len(input_arr) or j < 0 or j == len(input_arr[0]):
        return []
    elif int(input_arr[i][j]) == goal:   # found next num
        if goal == 9:
            #print(f"found 9 at {i},{j}")
            #print("found 9")
            return [i,j]
        else:
            return recur_find_all_paths(i-1, j, input_arr, nine_arr, goal+1) + recur_find_all_paths(i+1, j, input_arr, nine_arr, goal+1) + recur_find_all_paths(i, j-1, input_arr, nine_arr, goal+1) + recur_find_all_paths(i, j+1, input_arr, nine_arr, goal+1)
    else:
        return []

trailhead_sum = 0
for i, line in enumerate(input_arr):
    for j, ch in enumerate(line):
        if ch == '0':
            # start looking for all paths to 9
            arr = recur_find_all_paths(i, j, input_arr, [], 0)
            #print(f"array of 9s accessible from {i},{j}: {arr}")

            remove_dup_arr = []
            for k in range(0, len(arr), 2):
                el = [arr[k], arr[k+1]]
                #print(f"el: {el}")
                if el not in remove_dup_arr:
                    remove_dup_arr.append(el)
            
            #print(f"removed dups: {remove_dup_arr}")

            trailhead_sum += len(remove_dup_arr)

print(trailhead_sum)