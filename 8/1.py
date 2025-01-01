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
                        #print(f"match for {ch} at {i},{j} in {k},{l}")
                        diff_i = k - i
                        diff_j = l - j
                        i_after = k + diff_i
                        j_after = l + diff_j
                        i_before = i - diff_i
                        j_before = j - diff_j
                        if (j_before >= 0 and i_before >= 0) and (j_before < len(input_arr[0]) and i_before < len(input_arr)):
                            print(f"before: {i_before}, {j_before}")
                            frequency[i_before] = frequency[i_before][:j_before] + '#' + frequency[i_before][j_before+1:]
                        if (j_after < len(input_arr[0]) and i_after < len(input_arr)) and (j_after >= 0 and i_after >= 0):
                            #print(f"after: {i_after}, {j_after}")
                            frequency[i_after] = frequency[i_after][:j_after] + '#' + frequency[i_after][j_after+1:]


# count , 
comma_count = 0
for i in frequency:
    #print(i)
    for j in i:
        if j == '#':
            comma_count += 1

print(comma_count)