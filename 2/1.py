input_file = open("./input.txt", "r")
#print(input_file.readlines())

num = 0

for line in input_file:
    parts_str = line.strip().split(' ')
    #print(parts_str)
    parts = [int(i) for i in parts_str]
    #print(parts)
    if parts[1] - parts[0] > 0:
        #print("asc")
        parts_sorted = sorted(parts)
    else:
        #print("desc")
        parts_sorted = sorted(parts, reverse=True)
    #print("sorted list: ", parts_sorted)
    f = 0
    for i in range(len(parts)):
        #print(parts[i])
        #print(parts_sorted[i])
        if parts[i] != parts_sorted[i]: # break if not sorted
            f = 1
            break
    if f == 1:
        continue
    for i in range(1,len(parts)):
        diff = abs(int(parts[i] - parts[i-1]))
        if diff < 1 or diff > 3:
            f = 1
            break
    if f == 0:
        num += 1
    
print(num)
