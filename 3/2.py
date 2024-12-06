input_file = open("./input.txt", "r")
f = open("./logs-part2.txt", "w")
#print(input_file.readlines())

sum_of_multiply = 0

for line in input_file:
    print(line)
    f.write(f"line: {line}\n")
    # split by don't()
    dont_split = line.split("don't()")
    print("don't_split:", dont_split)
    f.write(f"don't_split:{dont_split}\n")
    for j, d in enumerate(dont_split):
        if j != 0:
            # split by do() and only take input after it
            do_split = d.split('do()')
            print("do_split for", d, "is", do_split)
            f.write(f"do_split for {d} is {do_split}\n")
            if len(do_split) == 1:
                continue
            d = ''.join(do_split[1:])
            # split by mul(
            mul_split = d.split('mul(')
        else:
            # split by mul(
            mul_split = d.split('mul(')
        print("mul_split for", dont_split[j], "is", mul_split)
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
                print("multiplying", first_num, "and", second_num)
                print("sum_of_multiply:", sum_of_multiply)
                f.write(f"multiplying {first_num} and {second_num}\n")
                f.write(f"sum_of_multiply: {sum_of_multiply}\n")
            except:
                continue
        
        f.write("\n")


    
print(sum_of_multiply)
