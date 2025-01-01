input_file = open("./eg-input.txt")
positions = []
velocity = []

for line in input_file:
    #input_arr.append(input_arr.strip())
    l = line.strip().split(" ")
    position_x = int(l[0].split("=")[-1].split(",")[1])
    position_y = int(l[0].split("=")[-1].split(",")[0])

    v_x = int(l[1].split("=")[-1].split(",")[1])
    v_y = int(l[1].split("=")[-1].split(",")[0])
    
    positions.append([position_x, position_y])
    velocity.append([v_x, v_y])

#print(positions)
#print(velocity)

# 101 wide, 103 tall max in input
# 11 wide, 7 tall
max_i = 7 #103
max_j = 11 #101

secs = 0
f = 1

mid_x = int(max_i / 2)
mid_y = int(max_j / 2)

print(mid_x, mid_y)

while f == 1 and secs < 1000000:
    f = 0
    final = []
    for i, position in enumerate(positions):
        #print(f"position: {position} and velocity: {velocity[i]}")

        final_x = (position[0] + velocity[i][0] * secs) % max_i
        final_y = (position[1] + velocity[i][1] * secs) % max_j

        #print(f"final position: {final_x}, {final_y}")
        final.append([final_x, final_y])

    #print(final)

    j = 1

    for l in range(max_i):
        for i in range(l, max_i):
            p = mid_y - j
            for k in range(max_j):
                #print(f"checking if 1 in {i},{k}")
                if k >= (mid_y - j) and k <= (mid_y + j):
                    if [i, k] in final:
                        continue
                    else:
                        print(f"1 not in {i},{k} but should be")
                        f = 1
                        break
                else:
                    if [i, k] in final:
                        print(f"1 in {i},{k} but shouldnt be")
                        f = 1
                        break

            if f == 1:
                break

            j += 2

        # if f == 1:
        #     break

    if f == 0:
        print(f"{secs} worked")
    else:
        print(f"{secs} secs didn't work")

    secs += 1