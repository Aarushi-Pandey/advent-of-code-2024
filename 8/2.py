input_file = open("./input.txt")
input_arr = []
frequency = []

for line in input_file:
    input_arr.append(line.strip())

frequency = input_arr[:]

print(f"i should be within 0 and {len(input_arr)}")
print(f"j should be within 0 and {len(input_arr[0])}")
#print(f"j should be within 0 and {len(input_arr[len(input_arr)-1])}")

for i, line in enumerate(input_arr):
    for j, ch in enumerate(line):
        if ch != '.': # check all frequency after it
            for k in range(len(input_arr)):
                for l in range(len(input_arr[0])):
                    el = input_arr[k][l]
                    if ch == el and (i != k and j != l):
                        # mark those 2 antennas as # too
                        frequency[i] = frequency[i][:j] + '#' + frequency[i][j+1:]
                        frequency[k] = frequency[k][:l] + '#' + frequency[k][l+1:]

                        #print(f"match for {ch} at {i},{j} in {k},{l}")
                        diff_i = k - i
                        diff_j = l - j
                        # keep finding coordinates until out of bounds
                        after_oob = 0
                        after_inc = 1
                        before_oob = 0
                        before_inc = 1
                        while after_oob == 0:
                            i_after = (diff_i * after_inc) + k
                            j_after = (diff_j * after_inc) + l
                            if (j_after < len(input_arr[0]) and i_after < len(input_arr)) and (j_after >= 0 and i_after >= 0):
                                #print(f"after: {i_after}, {j_after}")
                                frequency[i_after] = frequency[i_after][:j_after] + '#' + frequency[i_after][j_after+1:]
                            else:
                                after_oob = 1
                            after_inc += 1
                        
                        while before_oob == 0:
                            i_before = i - (diff_i * before_inc)
                            j_before = j - (diff_j * before_inc)
                            if (j_before >= 0 and i_before >= 0) and (j_before < len(input_arr[0]) and i_before < len(input_arr)):
                                #print(f"before: {i_before}, {j_before}")
                                frequency[i_before] = frequency[i_before][:j_before] + '#' + frequency[i_before][j_before+1:]
                            else:
                                before_oob = 1
                            before_inc += 1
                        


# count , 
comma_count = 0
for i in frequency:
    #print(i)
    for j in i:
        if j == '#':
            comma_count += 1

print(comma_count)