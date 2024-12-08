input_file = open("./input.txt", "r")

xmas_sum = 0
input_arr = []

# get input arr
for line in input_file:
    input_arr.append(line)

for i, line in enumerate(input_arr):
    for j, ch in enumerate(line):
        if ch == 'M' or ch == 'S':
            r = ch
            l = ""
            if j + 2 < len(line) and i + 2 < len(input_arr):
                r += input_arr[i+1][j+1]
                r += input_arr[i+2][j+2]
                l += input_arr[i+2][j]
                l += input_arr[i+1][j+1]
                l += input_arr[i][j+2]
                if (r == 'MAS' or r == 'SAM') and (l == 'MAS' or l == 'SAM'):
                    xmas_sum += 1


print(xmas_sum)
