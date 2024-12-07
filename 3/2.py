input_file = open("./input.txt", "r")
f = open("./logs-part2.txt", "w")
#print(input_file.readlines())

sum_of_multiply = 0
count = 1

for line in input_file:
    #print(line)
    f.write(f"line: {line}\n")
    # split by don't()
    dont_split = line.split("don't()")
    #print("don't_split:", dont_split)
    f.write(f"don't_split:{dont_split}\n") # eg: mul(a,b)don't()mul(c,d)do()mul(e,f) => ['mul(a,b)','mul(c,d)do()mul(e,f)']
    for j, d in enumerate(dont_split):
        if j != 0:
            f.write(f"all other parts should only take stuff after do()")
            # split by do() and only take input after it
            do_split = d.split('do()')
            #print("do_split for", d, "is", do_split)
            f.write(f"do_split for {d} is {do_split}\n")
            if len(do_split) == 1:
                continue
            d = ''.join(do_split[1:])
            # split by mul(
            mul_split = d.split('mul(')
            f.write(f"all other valid parts: {d}")
        else:
            f.write(f"first part shouldn't be skipped since this is before don't")
            f.write(f"first valid part: {d}")
            # split by mul(
            mul_split = d.split('mul(')
        #print("mul_split for", dont_split[j], "is", mul_split)
        f.write(f"mul_split for {dont_split[j]} is {mul_split}\n")

        # for each mul_split [except first one (whatever is before mul)]
        for i in range(1, len(mul_split)):
            # split by ,
            comma_split = mul_split[i].split(',')
            #print(comma_split)
            try:
                # check if spaces between numbers and commas and brackets
                if ' ' in comma_split[0] or ' ' in comma_split[1].split(')')[0]:
                    continue
                # convert first num to int
                first_num = int(comma_split[0])
                # get second num by getting str before ) and convert it to int
                second_num = int(comma_split[1].split(')')[0])

                sum_of_multiply += first_num * second_num
                #print("multiplying", first_num, "and", second_num)
                #print("sum_of_multiply:", sum_of_multiply)
                f.write(f"{count}: multiplying {first_num} and {second_num}\n")
                f.write(f"sum_of_multiply: {sum_of_multiply}\n")
                count += 1
            except:
                continue
        
        f.write("\n")


    
print(sum_of_multiply)
