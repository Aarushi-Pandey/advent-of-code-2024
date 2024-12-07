input_file = open("./input.txt", "r")
#print(input_file.readlines())

xmas_sum = 0
input_arr = []

print("left and right")
# sum of xmas
# sum of samx
for line in input_file:
    xmas_split = line.split('XMAS')
    #print(xmas_split)
    xmas_sum += len(xmas_split) - 1

    samx_split = line.split('SAMX')
    #print(samx_split)
    xmas_sum += len(samx_split) - 1

    input_arr.append(line)

    #print(f"sum = {xmas_sum}")

#print(input_arr)
print(f"sum so far = {xmas_sum}")

print("top and bottom")
# sum of xmas - down
# sum of xmas - up
for i in range(len(input_arr[0])): # each col
    vertical_str = ""
    for j in range(len(input_arr)):  # each row
        #print(f"{j},{i}: {input_arr[j][i]}")
        vertical_str += input_arr[j][i]

    #print(f"vertical str: {vertical_str}")
    
    xmas_split = vertical_str.split('XMAS')
    #print(xmas_split)
    xmas_sum += len(xmas_split) - 1

    samx_split = vertical_str.split('SAMX')
    #print(samx_split)
    xmas_sum += len(samx_split) - 1

    #print(f"sum = {xmas_sum}")

print(f"sum so far = {xmas_sum}")

print("right diagonal")
# sum of xmas - right diagonal
for i in range(len(input_arr)): # each row
    diff = i % (len(input_arr[i]) - 1)    # 0 mod 10
    if diff == 0:
        r = len(input_arr[i]) - 1
    else:
        r = 1   # only get diagonal from 1st element
    #print(f"r = {r}")
    for j in range(r): # each col until row index reached # starting index = arr[i][j] = 1,0   
        diagonal_str = ""
        #print(f"i,j = {i},{j}")
        # if diff == 0:
        #     r2 = len(input_arr[i])-j-1
        # else:
        #     r2 = j
        for k in range(len(input_arr[i])-j-1): # each diagonal starting point -> input_arr[i][j] till [i+n][k+n] 1,0 till 10,9
            if i + k >= len(input_arr[i])-1:
                break
            #print(f"k: {k}, i+k: {i+k}")
            el = input_arr[i+k][j+k]
            diagonal_str += el
        
        #print(f"diagonal: {diagonal_str}")
        
        xmas_split = diagonal_str.split('XMAS')
        #print(xmas_split)
        xmas_sum += len(xmas_split) - 1

        samx_split = diagonal_str.split('SAMX')
        #print(samx_split)
        xmas_sum += len(samx_split) - 1

        #print(f"sum = {xmas_sum}")

print(f"sum so far = {xmas_sum}")

print("left diagonal")
# reverse each row and col order and do the same thing as right diagonal check
input_arr.reverse()
for i in range(len(input_arr)):
    input_arr[i] = input_arr[i][::-1].strip()
#print(f"reversed matrix: {input_arr}")

for i in range(len(input_arr)): # each row
    diff = i % (len(input_arr[i]))    # 0 mod 10
    if diff == 0:
        r = len(input_arr[i])
    else:
        r = 1   # only get diagonal from 1st element
    #print(f"r = {r}")
    for j in range(r): # each col until row index reached # starting index = arr[i][j] = 1,0   
        diagonal_str = ""
        #print(f"i,j = {i},{j}")
        # if diff == 0:
        #     r2 = len(input_arr[i])-j-1
        # else:
        #     r2 = j
        for k in range(len(input_arr[i])-j): # each diagonal starting point -> input_arr[i][j] till [i+n][k+n] 1,0 till 10,9
            if i + k >= len(input_arr[i]):
                break
            #print(f"k: {k}, i+k: {i+k}")
            el = input_arr[i+k][j+k]
            diagonal_str += el
        
        #print(f"diagonal: {diagonal_str}")
        
        xmas_split = diagonal_str.split('XMAS')
        #print(xmas_split)
        xmas_sum += len(xmas_split) - 1

        samx_split = diagonal_str.split('SAMX')
        #print(samx_split)
        xmas_sum += len(samx_split) - 1

        #print(f"sum = {xmas_sum}")
    
print(xmas_sum)