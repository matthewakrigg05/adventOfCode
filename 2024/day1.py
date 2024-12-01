def getPairs():
    leftList = []
    rightList = []

    with open("./in.txt", "r") as input:
        lines = input.readlines()
        for line in lines:
            line = line.strip("\n").split("   ")
            leftList.append(int(line[0]))
            rightList.append(int(line[1]))

    return sorted(leftList), sorted(rightList)

left, right = getPairs()
print(sum(abs(x - y) for x, y in zip(left, right)))
print(sum(x for x in right if x in left))

