input_file = open("./input.txt")
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

final = []

# 101 wide, 103 tall max in input
# 11 wide, 7 tall
max_i = 103
max_j = 101

for i, position in enumerate(positions):
    #print(f"position: {position} and velocity: {velocity[i]}")

    final_x = (position[0] + velocity[i][0] * 100) % max_i
    final_y = (position[1] + velocity[i][1] * 100) % max_j

    #print(f"final position: {final_x}, {final_y}")
    final.append([final_x, final_y])

print(final)

mid_x = int(max_i / 2)
mid_y = int(max_j / 2)

print(mid_x, mid_y)

q1, q2, q3, q4 = 0, 0, 0, 0

for f in final:
    if f[0] < mid_x and f[1] < mid_y: #q1
        q1 += 1
    elif f[0] > mid_x and f[1] < mid_y: #q3
        q3 += 1
    elif f[0] < mid_x and f[1] > mid_y: #q2
        q2 += 1
    elif f[0] > mid_x and f[1] > mid_y: #q4
        q4 += 1

print(q1*q2*q3*q4)