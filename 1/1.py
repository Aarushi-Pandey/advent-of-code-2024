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

#print(arr1)
# sort each list
arr1.sort()
arr2.sort()

#print(arr1)
# go through each list, find diff and keep sum variable
sum_of_diff = 0

for i in range(0, len(arr1)):
    #print(int(arr1[i]))
    sum_of_diff += abs(int(arr1[i]) - int(arr2[i]))

print(sum_of_diff)