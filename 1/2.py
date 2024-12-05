# read input and for each line, add first no to arr1 and second no to arr2
input_file = open("./1-input.txt", "r")
#print(input_file.readlines())

arr1 = []
arr2 = []
for i in input_file.readlines():
    if not i.strip():
        continue
    #print(i)
    #print(i.split(' '))
    arr1.append(i.split(' ')[0])
    arr2.append(i.split(' ')[3])

#improvement: use open function and then use strip() then split() functions

sum_of_multiplication = 0

for i in arr1:
    n = 0
    for j in arr2:
        if int(i) == int(j):
            n += 1
        
    #print(int(i), n)
    sum_of_multiplication += int(i)*n

#print(sum_of_multiplication)