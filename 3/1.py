input_file = open("./input.txt", "r")
#print(input_file.readlines())

sum_of_multiply = 0

for line in input_file:
    mul_split = line.split('mul(')
    #print(mul_split)

    for i in range(1, len(mul_split)):
        comma_split = mul_split[i].split(',')
        #print(comma_split)
        try:
            first_num = int(comma_split[0])
            second_num = int(comma_split[1].split(')')[0])
            sum_of_multiply += first_num * second_num
        except:
            continue


    
print(sum_of_multiply)
