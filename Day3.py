f = open("inputDay3.txt")

content = f.readlines()
total = 0

# part 2
for line in content:
    line = list(line)
    line = line[0 : len(line) - 1]
    finalAns = []
    index = -1
    prevIndex = 0
    for i in range(11, -1, -1):
        high = max(line[prevIndex + index + 1 : len(line) - i])
        prevIndex += index + 1
        index = line[prevIndex:].index(str(high))
        finalAns.append(high)
    finalAns = "".join(finalAns)
    total += int(finalAns)


# for line in content:
#     line = list(line)
#     line = line[0 : len(line) - 1]
#     firstHigh = max(line[0 : len(line) - 1])
#     index = line.index(str(firstHigh))
#     secondHigh = max(line[index + 1 :])
#     final = str(firstHigh) + str(secondHigh)
#     total += int(final)


f.close()
print(total)
