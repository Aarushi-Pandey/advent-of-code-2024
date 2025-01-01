
def recur_check_result_possible(res, curr_calc, inp, chosen_calc):
    if inp == []:
        if curr_calc == res:
            return True
        else:
            return False
    else:
        return recur_check_result_possible(res, curr_calc * inp[0], inp[1:], '*') or recur_check_result_possible(res, curr_calc + inp[0], inp[1:], '+')

input_file = open("./input.txt")

required_result = []
inputs = []

for line in input_file:
    l = line.split(":")
    required_result.append(int(l[0]))
    inp = []
    for i in l[1].strip().split(' '):
        inp.append(int(i))
    inputs.append(inp)

#print(required_result)
#print(inputs)

# + + + # num_of_* = 0, position = -1
# * + + # num_of_* = 1, position = 0
# + * + # num_of_* = 1, position = 1
# + + * # num_of_* = 1, position = 2
# * * + # num_of_* = 2, position = 0,1
# * + * # num_of_* = 2, position = 0,2
# + * * # num_of_* = 2, position = 1,2
# * * * # num_of_* = 3, position = 0,1,2

sum_of_true_results = 0

for i, r in enumerate(required_result):
    inp = inputs[i]
    # have to do recursion :/
    check_if_possible = recur_check_result_possible(r, inp[0], inp[1:], '*')
    if check_if_possible:
        sum_of_true_results += r
        #print(f"result is good: {r}")

print(sum_of_true_results)