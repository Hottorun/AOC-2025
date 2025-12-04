f = open("inputDay4.txt")

content = f.readlines()
total = 0
multArray = []
toBeRemoved = []
removedSmth = True

for line in content:
    line = list(line)
    line = line[: len(line) - 1]
    multArray.append(line)

while removedSmth:
    removedSmth = False
    for i in range(len(multArray)):
        for j in range(len(multArray[0])):
            if multArray[i][j] == "@":
                start_l = j - 1
                start_t = i - 1
                end_r = j + 1
                end_b = i + 1
                checkList = []

                if start_l < 0:
                    start_l = 0
                    checkList += multArray[i][end_r]
                elif end_r == len(multArray[0]):
                    end_r = j
                    checkList += multArray[i][start_l]
                else:
                    checkList += multArray[i][start_l]
                    checkList += multArray[i][end_r]

                if start_t < 0:
                    start_t = 0
                    checkList += multArray[i + 1][start_l : end_r + 1]
                elif end_b == len(multArray):
                    end_b = i
                    checkList += multArray[i - 1][start_l : end_r + 1]
                else:
                    checkList += multArray[i - 1][start_l : end_r + 1]
                    checkList += multArray[i + 1][start_l : end_r + 1]

                if checkList.count("@") < 4:
                    removedSmth = True
                    total += 1
                    toBeRemoved.append([i, j])

    for item in toBeRemoved:
        multArray[item[0]][item[1]] = "."
    toBeRemoved = []


# try 1
# for line in content:
#     line = list(line)
#     line = line[: len(line) - 1]
#     for index, ch in enumerate(line):
#         if ch == "@":
#             # start of line (0123 num)
#             print(index)
#             if index < 4:
#                 new_part = line[0:index] + line[index + 1 : index + 5]
#                 print(new_part)
#                 if new_part.count("@") <= 4:
#                     print("yes")
#                     total += 1
#             # end of line ( num     96 97 98 99
#             # last index = len(line)-1
#             elif index > len(line) - 5:
#                 new_part = line[index - 4 : index] + line[index + 1 :]
#                 print(new_part)
#                 if new_part.count("@") <= 4:
#                     print("yes")
#                     total += 1
#             else:
#                 new_part = line[index - 4 : index] + line[index + 1 : index + 5]
#                 print(new_part)
#                 if new_part.count("@") <= 4:
#                     print("yes")
#                     total += 1
print(total)
f.close()
