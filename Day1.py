f = open("inputDay1.txt")
current = 50
answer = 0
for line in f.readlines():
    if line == "":
        break
    chars = list(line)
    if chars[0] == "R":
        chars.pop(0)
        chars = "".join(chars)
        for i in range(0, int(chars)):
            current += 1
            if current == 100:
                current = 0
            if current == 0:
                answer += 1

    else:
        chars.pop(0)
        chars = "".join(chars)
        for i in range(0, int(chars)):
            current -= 1
            if current == 0:
                answer += 1
            if current == -1:
                current = 99

f.close()
print(answer)
