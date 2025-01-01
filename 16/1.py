import sys

input_file = open("./input.txt")
input_arr = []

for line in input_file:
    input_arr.append(line.strip())

# find start position
start_i, start_j = -1, -1
for i, line in enumerate(input_arr):
    for j, ch in enumerate(line):
        if ch == 'S':
            start_i = i
            start_j = j 
            break

# increase recursion limit
sys.setrecursionlimit(3000)


print(start_i, start_j)

def recur_find_end(i, j, input_arr, direction, travelled_arr):
    #print(i, j)
    if input_arr[i][j] == '#' or [i,j] in travelled_arr:
        return 100000000 #big number, not possible path OR already travelled path
    elif input_arr[i][j] == 'E':
        return 0    #reached end
    else:
        travelled_arr.append([i,j])
        if direction == 'R':
            # too many recursion loops so check beforehand
            min_r, min_l, min_u, min_d = 100000000, 100000000, 100000000, 100000000
            if not (input_arr[i+1][j] == '#' or [i+1, j] in travelled_arr):
                min_u = 1001 + recur_find_end(i+1, j, input_arr, 'U', travelled_arr[:])
            if not (input_arr[i-1][j] == '#' or [i-1, j] in travelled_arr):
                min_d = 1001 + recur_find_end(i-1, j, input_arr, 'D', travelled_arr[:])
            if not (input_arr[i][j-1] == '#' or [i, j-1] in travelled_arr):
                min_l = 2001 + recur_find_end(i, j-1, input_arr, 'L', travelled_arr[:])
            if not (input_arr[i][j+1] == '#' or [i, j+1] in travelled_arr):
                min_r = 1 + recur_find_end(i, j+1, input_arr, 'R', travelled_arr[:])
            return min(min_u, min_d, min_l, min_r)
        
        elif direction == 'L':
            # too many recursion loops so check beforehand
            min_r, min_l, min_u, min_d = 100000000, 100000000, 100000000, 100000000
            if not (input_arr[i+1][j] == '#' or [i+1, j] in travelled_arr):
                min_u = 1001 + recur_find_end(i+1, j, input_arr, 'U', travelled_arr[:])
            if not (input_arr[i-1][j] == '#' or [i-1, j] in travelled_arr):
                min_d = 1001 + recur_find_end(i-1, j, input_arr, 'D', travelled_arr[:])
            if not (input_arr[i][j-1] == '#' or [i, j-1] in travelled_arr):
                min_l = 1 + recur_find_end(i, j-1, input_arr, 'L', travelled_arr[:])
            if not (input_arr[i][j+1] == '#' or [i, j+1] in travelled_arr):
                min_r = 2001 + recur_find_end(i, j+1, input_arr, 'R', travelled_arr[:])
            return min(min_u, min_d, min_l, min_r)

        elif direction == 'U':
            # too many recursion loops so check beforehand
            min_r, min_l, min_u, min_d = 100000000, 100000000, 100000000, 100000000
            if not (input_arr[i+1][j] == '#' or [i+1, j] in travelled_arr):
                min_u = 1 + recur_find_end(i+1, j, input_arr, 'U', travelled_arr[:])
            if not (input_arr[i-1][j] == '#' or [i-1, j] in travelled_arr):
                min_d = 2001 + recur_find_end(i-1, j, input_arr, 'D', travelled_arr[:])
            if not (input_arr[i][j-1] == '#' or [i, j-1] in travelled_arr):
                min_l = 1001 + recur_find_end(i, j-1, input_arr, 'L', travelled_arr[:])
            if not (input_arr[i][j+1] == '#' or [i, j+1] in travelled_arr):
                min_r = 1001 + recur_find_end(i, j+1, input_arr, 'R', travelled_arr[:])
            return min(min_u, min_d, min_l, min_r)

        else:
            # too many recursion loops so check beforehand
            min_r, min_l, min_u, min_d = 100000000, 100000000, 100000000, 100000000
            if not (input_arr[i+1][j] == '#' or [i+1, j] in travelled_arr):
                min_u = 2001 + recur_find_end(i+1, j, input_arr, 'U', travelled_arr[:])
            if not (input_arr[i-1][j] == '#' or [i-1, j] in travelled_arr):
                min_d = 1 + recur_find_end(i-1, j, input_arr, 'D', travelled_arr[:])
            if not (input_arr[i][j-1] == '#' or [i, j-1] in travelled_arr):
                min_l = 1001 + recur_find_end(i, j-1, input_arr, 'L', travelled_arr[:])
            if not (input_arr[i][j+1] == '#' or [i, j+1] in travelled_arr):
                min_r = 1001 + recur_find_end(i, j+1, input_arr, 'R', travelled_arr[:])
            return min(min_u, min_d, min_l, min_r)

        
print(recur_find_end(start_i, start_j, input_arr, 'R', []))