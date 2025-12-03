f = open("inputDay2.txt")
content = f.readline()
content = content.split(",")
countId = 0
for nums in content:
    nums = nums.split("-")
    firstVal: int = int(nums[0])
    secondVal: int = int(nums[1]) + 1
    for i in range(firstVal, secondVal):
        print("i", i)
        for pattern in range(1, int(len(str(i)) / 2) + 1):
            pattern = str(i)[0:pattern]
            print("pattern", pattern)
            isTrue = True
            for index in range(len(str(pattern)), len(str(i)), len(str(pattern))):
                print("index", index)
                print("goofy string", str(i)[index : index + len(str(pattern))])
                if pattern != str(i)[index : index + len(str(pattern))]:
                    isTrue = False
            if isTrue:
                countId += i
                print(i)
                break

        # first part
        # if len(str(i)) % 2 == 0:
        #     # smth smth, repeating digit
        #     length: int = int(len(str(i)) / 2)
        #     firstPart = str(i)[0:length]
        #     if firstPart == str(i)[length:]:
        #         countId += i
        #         print(i)


print(countId)
