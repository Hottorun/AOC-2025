f = open("inputDay3.txt")

content = f.readlines()
total = 0
for line in content:
    line = list(line)
    line = line[0 : len(line) - 1]
    firstHigh = max(line[0 : len(line) - 1])
    index = line.index(str(firstHigh))
    secondHigh = max(line[index + 1 :])
    final = str(firstHigh) + str(secondHigh)
    total += int(final)

f.close()
print(total)
