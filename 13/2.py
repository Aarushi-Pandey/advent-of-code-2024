input_file = open("./eg-input.txt")
a_coord = []
b_coord = []
p_coord = []

for line in input_file:
    l = line.strip()
    if l == '':
        continue
    elif "Button A" in l:
        l_split = l.split(" ")
        #print(l_split)
        x = int(l_split[2].split("+")[-1][:-1])
        y = int(l_split[3].split("+")[-1])
        #print(x)
        #print(y)
        a_coord.append([x,y])
    elif "Button B" in l:
        l_split = l.split(" ")
        #print(l_split)
        x = int(l_split[2].split("+")[-1][:-1])
        y = int(l_split[3].split("+")[-1])
        #print(x)
        #print(y)
        b_coord.append([x,y])
    elif "Prize" in l:
        l_split = l.split(" ")
        #print(l_split)
        x = int(l_split[1].split("=")[-1][:-1]) #+ 10000000000000
        y = int(l_split[2].split("=")[-1]) #+ 10000000000000
        #print(x)
        #print(y)
        p_coord.append([x,y])

total_token_count = 0

for i in range(len(p_coord)):
    a_x, a_y = a_coord[i][0], a_coord[i][1]
    b_x, b_y = b_coord[i][0], b_coord[i][1]
    p_x, p_y = p_coord[i][0], p_coord[i][1]

    #print(f"a: {a_x}, {a_y}")
    #print(f"b: {b_x}, {b_y}")
    #print(f"p: {p_x}, {p_y}")

    #max_attempt = 10000000000000
    current_fewest_tokens_needed = 10000000000000 * 3

    # try with controlling a count
    #for j in range(max_attempt):
    #desired_p_x, desired_p_y = p_x - (j * a_x), p_y - (j * a_y)

    # check if divisible by b and remainder either divisible by (a+b) or a
    # remainder_x_b, remainder_y_b = p_x % , p_y % b_y
    print(f"dividing by b gives remainder {remainder_x_b} and {remainder_y_b}")
    remainder_x_combo, remainder_y_combo = remainder_x_b % (a_x + b_x), remainder_y_b % (a_y + b_y)
    print(f"dividing that by combo gives remainder {remainder_x_combo} and {remainder_y_combo}")
    remainder_x_a, remainder_y_a = remainder_x_combo % a_x, remainder_y_combo % a_y
    print(f"dividing that by a gives remainder {remainder_x_a} and {remainder_y_a}")

    if remainder_x_a == 0 and remainder_y_a == 0 and p_x/b_x == p_y/b_y and remainder_x_b/(a_x+b_x) == remainder_y_b/(a_y+b_y) and remainder_x_combo/a_x == remainder_y_combo/a_y:
        print("success at 1st")
        token_count = 3 * remainder_x_combo/a_x + 1 * p_x/b_x + 4 * (remainder_x_b/(a_x+b_x))
        if token_count < current_fewest_tokens_needed:
            current_fewest_tokens_needed = token_count

    # check if divisible by a and remainder either divisible by (a+b) or b
    remainder_x_a, remainder_y_a = p_x % a_x, p_y % a_y
    print(f"dividing by a gives remainder {remainder_x_a} and {remainder_y_a}")
    remainder_x_combo, remainder_y_combo = remainder_x_a % (a_x + b_x), remainder_y_a % (a_y + b_y)
    print(f"dividing that by combo gives remainder {remainder_x_combo} and {remainder_y_combo}")
    remainder_x_b, remainder_y_b = remainder_x_combo % b_x, remainder_y_combo % b_y
    print(f"dividing that by a gives remainder {remainder_x_b} and {remainder_y_b}")

    if remainder_x_b == 0 and remainder_y_b == 0 and p_x/a_x == p_y/a_y and remainder_x_a/(a_x+b_x) == remainder_y_a/(a_y+b_y) and remainder_x_combo/b_x == remainder_y_combo/b_y:
        print("success at 2nd")
        token_count = 1 * remainder_x_combo/b_x + 3 * p_x/a_x + 4 * (remainder_x_a/(a_x+b_x))
        if token_count < current_fewest_tokens_needed:
            current_fewest_tokens_needed = token_count

    # check if divisible by (a+b) and remainder either divisible by a or b
    remainder_x_ab, remainder_y_ab = p_x % (a_x+b_x), p_y % (a_y+b_y)
    print(f"dividing by a+b gives remainder {remainder_x_ab} and {remainder_y_ab}")
    remainder_x_b, remainder_y_b = remainder_x_ab % (b_x), remainder_y_ab % (b_y)
    print(f"dividing that by b gives remainder {remainder_x_b} and {remainder_y_b}")
    remainder_x_a, remainder_y_a = remainder_x_b % a_x, remainder_y_b % a_y
    print(f"dividing that by a gives remainder {remainder_x_a} and {remainder_y_a}")

    if remainder_x_a == 0 and remainder_y_a == 0 and p_x/(a_x+b_x) == p_y/(a_y+b_y) and remainder_x_ab/(b_x) == remainder_y_ab/(b_y) and remainder_x_b/a_x == remainder_y_b/a_y:
        print("success at 3rd")
        token_count = 1 * remainder_x_ab/b_x + 3 * remainder_x_b/a_x + 4 * (p_x/(a_x+b_x))
        if token_count < current_fewest_tokens_needed:
            current_fewest_tokens_needed = token_count

    if current_fewest_tokens_needed == 30000000000000:
        print(f"no route found for prize {p_coord[i]}")
        continue

    total_token_count += current_fewest_tokens_needed
    print(current_fewest_tokens_needed)

print(total_token_count)

