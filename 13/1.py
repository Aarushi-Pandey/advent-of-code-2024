input_file = open("./input.txt")
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
        x = int(l_split[1].split("=")[-1][:-1])
        y = int(l_split[2].split("=")[-1])
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

    max_attempt = 100
    current_fewest_tokens_needed = 500

    # try with controlling a count
    for j in range(max_attempt):
        desired_p_x, desired_p_y = p_x - (j * a_x), p_y - (j * a_y)
        #print(f"{desired_p_x}, {desired_p_y}")
        if desired_p_x > 0 and desired_p_x % b_x == 0 and desired_p_x/b_x <= 100 and desired_p_y > 0 and desired_p_y % b_y == 0 and desired_p_y/b_y <= 100 and desired_p_x/b_x == desired_p_y/b_y:   # found coord match
            print(f"found coord match for no of b tokens = {int(desired_p_x/b_x)} and no of a token = {j}")
            token_count = 3 * j + 1 * int(desired_p_x / b_x)
            if token_count < current_fewest_tokens_needed:
                current_fewest_tokens_needed = token_count

    if current_fewest_tokens_needed == 500:
        print(f"no route found for prize {p_coord[i]}")
        continue

    total_token_count += current_fewest_tokens_needed
    print(current_fewest_tokens_needed)

print(total_token_count)

