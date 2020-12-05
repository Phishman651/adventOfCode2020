print("Advent of Code 2020")
print('User: Phishman651')
print('Day 1 Part 1')

f = open("day1Input.txt","r")

myList = []
# print("myList:")
# print(myList)

for line in f:
    myList.append(line)

# print("myList:")
# print(myList)

lst = []
for i in myList:
    i = i[:-1]
    lst.append(int(i))

# print("lst:")
# print(lst)

# print(len(lst))
# print(lst[0])
# print(lst[1])
# print(lst[199])

for i in range(len(lst)):
    print(str(i) + " :   " + str(lst[i]))

    tmp = lst[i]
    diff = 2020 - tmp
    # print("2020 - " + str(lst[i]) + " = " + str(diff))
    if diff in lst:
        print("2020 - " + str(lst[i]) + " = " + str(diff))
        print("This entry " + str(lst[i]) + "(index " + str(i) + ") and " + str(diff) + "(index " + str(lst.index(diff)) + ") are both found in the list")
        key = tmp * diff
        print("Multiplying them together gives " + str(tmp) + " * " + str(diff) + " = " + str(key))
        # print(lst.index(diff))
        break