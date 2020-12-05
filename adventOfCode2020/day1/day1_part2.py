print("Advent of Code 2020")
print('User: Phishman651')
print('Day 1 Part 2')

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

# for i in range(len(lst)):
#     # print("i = " + str(i) + " :   " + str(lst[i]))

#     firstNum = lst[i]
#     remaining = 2020 - firstNum
#     # print("First number: " + str(firstNum))
#     # print("Remaining amount (2020 - firstNum): " + str(remaining))

#     for j in range(len(lst)):
#         # print("j = " + str(j) + " :   " + str(lst[j]))
#         if (j != i):
#             secondNum = lst[j]
#             if (secondNum <= remaining):
#                 remaining = 2020 - firstNum - secondNum
#                 # print("Second number: " + str(secondNum))
#                 # print("Remaining amount (2020 - firstNum - secondNum): " + str(remaining))

#                 if remaining in lst:
#                     print("remaining is here " + str(remaining))

#                 for k in range(len(lst)):
#                     # print("k = " + str(k) + " :   " + str(lst[k]))
#                     if ((k != i) or (k != j)):
#                         thirdNum = lst[k]
#                         if (thirdNum <= remaining):
#                             sum = firstNum + secondNum + thirdNum
#                             # print("First number: " + str(firstNum))
#                             # print("Second number: " + str(secondNum))
#                             # print("Third number: " + str(thirdNum))
#                             # print("Sum: " + str(sum))
#                             # print("")
#                             if (sum == 2020):
#                                 print("First number: " + str(firstNum))
#                                 print("Second number: " + str(secondNum))
#                                 print("Third number: " + str(thirdNum))
#                                 print("Sum: " + str(sum))
#                                 print("")

for i in range(len(lst))    :
    for j in range(len(lst)):
        for k in range(len(lst)):
            if((lst[i] + lst[j] + lst[k]) == 2020):
                answer = lst[i] * lst[j] * lst[k]
                print("first number: " + str(lst[i]) + ", second number: " + str(lst[j]) + ", third number: " + str(lst[k]))
                print("sum = " + str(lst[i]) + " + " + str(lst[j]) + " + " + str(lst[k]) + " = " + str(lst[i] + lst[j] + lst[k]))
                print("product = " + str(lst[i]) + " x " + str(lst[j]) +  " x " + str(lst[k]) +" = " + str(lst[i] * lst[j] * lst[k]))
                            



    # if diff in lst:
    #     print("2020 - " + str(lst[i]) + " = " + str(diff))
    #     print("This entry " + str(lst[i]) + "(index " + str(i) + ") and " + str(diff) + "(index " + str(lst.index(diff)) + ") are both found in the list")
    #     key = tmp * diff
    #     print("Multiplying them together gives " + str(tmp) + " * " + str(diff) + " = " + str(key))
    #     # print(lst.index(diff))
    #     break