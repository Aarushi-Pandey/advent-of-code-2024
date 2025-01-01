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
            spread_file.append([int(i/2), int(num)])
        else:
            #print('.' * (int(num)))
            if (int(num) != 0):
                spread_file.append([-1, int(num)])

    print(spread_file)
    spread_file_arr.append(spread_file)

    f.write(f"{spread_file}\n")

for s in spread_file_arr:
    j = len(s)-1
    while j >= 0:
        while j >=0 and s[j][0] == -1 or s[j][1] == 0:
            j -= 1
        f.write(f"aiming to move {s[j]} forward")
        for i in range(j):
            #print(f"i,j = {i},{j}")
            if s[i][0] == -1 and s[j][1] <= s[i][1]:
                #print(f"{s[j]} can be moved to {i} position, replacing {s[i]}")
                #print(f"{ch}")

                file = s[i][:]

                s[i] = s[j][:] #+ ((len(s[i]) - len(s[j])) * '.')
                if file[1] - s[j][1] > 0:
                    s.insert(i+1, [-1, (file[1] - s[j][1])])
                    #print(f"new s: {s}")
                    j += 1

                s[j][0] = -1
                
                # combine '.' nearby
                if j+1 < len(s) and s[j+1][0] == -1:
                    #print(f"combining with j+1")
                    s[j][1] += s[j+1][1]
                    s[j+1][1] = 0
                if j-1 >= 0 and s[j-1][0] == -1:
                    #print(f"combining with j-1")
                    s[j][1] += s[j-1][1]
                    s[j-1][1] = 0

                #print(f"s[j] is now {s[j]}")
                #s[j] = '.' * len(s[j])
                # j -= 1
                # i += 1

                #print(f"updated s: {s}")

                break #should be break?
            # else:
            #     print(f"{s[j]} can't be moved to {i} position and replace {s[i]}")
            #     j -= 1
            
        #print(s)
        j -= 1
    #print(s) 
    f.write(f"{s}")

    #get checksum
    checksum = 0
    index = 0
    for i in range(len(s)):
        if s[i][1] == 0:
            continue
        if s[i][0] == -1:
            index += s[i][1]
        else:
            for k in range(s[i][1]):
                checksum += s[i][0] * (k + index)
            index += s[i][1]

    print(checksum)