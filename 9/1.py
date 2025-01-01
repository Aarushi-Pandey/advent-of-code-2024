input_file = open("./input.txt")
f = open("./debug.txt", "w")

input_arr = []
for line in input_file:
    input_arr.append(line.strip())

spread_file_arr = []
for inp in input_arr:
    spread_file = []
    for i, num in enumerate(inp):
        #print(num)
        if i % 2 == 0:
            #print(f"{num} ch copied {int(i/2)} times is {str(int(i/2)) * int(num)}")
            for j in range(int(num)):
                spread_file.append(str(int(i/2)))
        else:
            #print('.' * (int(num)))
            for j in range(int(num)):
                spread_file.append('.')

    #print(spread_file)
    spread_file_arr.append(spread_file)

    f.write(f"{spread_file}")

for s in spread_file_arr:
    j = len(s)-1
    for i, ch in enumerate(s):
        while s[j] == '.':
            j -= 1
        if ch == '.' and j > i:
            #print(f"{ch}")
            s[i] = s[j]
            s[j] = '.'
            j -= 1
        #else:
            #print("no change")
        #print(s)
    print(s) 

    # get checksum
    checksum = 0
    for i, ch in enumerate(s):
        if ch == '.':
            continue
        checksum += i * int(ch)

    print(checksum)