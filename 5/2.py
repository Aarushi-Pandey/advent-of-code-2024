input_file = open("./input.txt", "r")

middle_el_sum = 0
rules = []
input_arr = []

# get rules
for line in input_file:
    if line == '\n':  # reached second part of input
        break
    
    r_arr = []
    for i in line.strip().split('|'):
        r_arr.append(int(i))
    
    rules.append(r_arr)

#print(f"rules: {rules}")

# get input
for line in input_file:
    r = line.strip().split(',')
    #print(r)
    
    if len(r) == 1: # reached second part of input
        continue
    
    input_arr.append(r)  

input_arr_int = []  

for inp in input_arr:
    input_arr_int.append([int(j) for j in inp])

#print(f"input_arr: {input_arr_int}")

# check all rules for each input line
for index, inp in enumerate(input_arr_int): # each input
    #print(inp)
    inp_tmp = inp
    fl = 0
    f = 1
    while f == 1:
        #print(f"current input: {inp}") # 75 47 61 53 29
        f = 0
        for i in range(len(inp)):   # current number
            curr = inp[i]
            for j in range(i+1, len(inp)):  # numbers after it
                el = inp[j]
                # check if opposing rule
                for r in rules:
                    if el == r[0] and curr == r[1]:
                        fl = 1
                        f = 1
                        inp.insert(i, el)
                        inp.pop(j+1)
        
    if fl == 1:
        #print(f"invalid turned valid: {inp_tmp}, index: {index}")
        middle_el = inp[int(len(inp)/2)]
        middle_el_sum += middle_el
                    

print(middle_el_sum)
