input_file = open("./eg2-input.txt")
input_arr = []

for line in input_file:
    input_arr.append(line.strip())

def recur_find_len_area(i, j, input_arr, peri, area, ch, travelled_arr):
    #print(f"{i},{j}")
    if i < 0 or i == len(input_arr) or j < 0 or j == len(input_arr[0]):
        return 0, 0
    else:
        if input_arr[i][j] == ch:
            #print(f"{i},{j} matches {ch}")
            if [i, j] not in travelled_arr:
                travelled_arr.append([i,j])
                peri1, area1 = recur_find_len_area(i+1, j, input_arr, peri, area, ch, travelled_arr)
                peri2, area2 = recur_find_len_area(i-1, j, input_arr, peri, area, ch, travelled_arr)
                peri3, area3 = recur_find_len_area(i, j+1, input_arr, peri, area, ch, travelled_arr)
                peri4, area4 = recur_find_len_area(i, j-1, input_arr, peri, area, ch, travelled_arr)

                # final_perimeter = 4

                # if peri1 > 0:
                #     final_perimeter = final_perimeter - 1 + 3
                # if peri2 > 0:
                #     final_perimeter = final_perimeter - 1 + 3
                # if peri3 > 0:
                #     final_perimeter = final_perimeter - 1 + 3
                # if peri4 > 0:
                #     final_perimeter = final_perimeter - 1 + 3

                #curr_perimeter = peri - (peri1 + peri2 + peri3 + peri4)
                #curr_area = area1 + area2 + area3 + area4

                # print(f"{i},{j}: {final_perimeter}, {area}")

                
                #curr_perimeter = peri - (area1 + area2 + area3 + area4) + 4 - (area1 + area2 + area3 + area4) # how many boundaries the current element needs

                # if peri1:
                #     curr_perimeter += peri1 - 1
                # if peri2:
                #     curr_perimeter += peri2 - 1
                # if peri3:
                #     curr_perimeter += peri3 - 1
                # if peri4:
                #     curr_perimeter += peri4 - 1

                #print(f"perimeter at {i},{j} : {curr_perimeter}")


                return travelled_arr, 1 + (area1 + area2 + area3 + area4)
            else:
                return 0, 0
        else:
            return 0, 0



peri_area_arr = {}

sum_peri_area = 0

for k, line in enumerate(input_arr):
    for l, ch in enumerate(line):
        check_if_ch_exists = ch not in peri_area_arr
        check_if_travelled = False
        if not check_if_ch_exists:
            for block in peri_area_arr[ch]:
                #print(f"block: {block}")
                if [k,l] in block[2]:
                    check_if_travelled = True
                    break

        if check_if_ch_exists or not check_if_travelled:
            print(f"{ch} in {k},{l}")
            travelled_arr, area = recur_find_len_area(k, l, input_arr, 0, 1, ch, [])
            #print(travelled_arr)

            peri = len(travelled_arr) * 4
            #print(f"init peri: {peri}")
            # subtract 1 from perimeter for each neighbor it has
            for ind in travelled_arr:
                i = ind[0]
                j = ind[1]
                if [i+1, j] in travelled_arr:
                    peri -= 2
                if [i-1, j] in travelled_arr:
                    peri -= 2
                if [i, j+1] in travelled_arr:
                    peri -= 2
                if [i, j-1] in travelled_arr:
                    peri -= 2

            #sorted_travelled_arr = sorted(travelled_arr[:])

            if ch not in peri_area_arr:
                peri_area_arr[ch] = [[peri, area, travelled_arr]]
            else:
                peri_area_arr[ch].append([peri, area, travelled_arr])
            print(f"{peri} * {area}")
            #sum_peri_area += peri * area

print(sum_peri_area)