with open("in.txt") as f:
    inp = f.readlines()
    count = 0

    # map the contents of the input using dict so directions can be clarified
    dict = {(y, x): inp[y][x] for y in range(len(inp)) for x in range(len(inp[0]) - 1)}
    directions = [(dy, dx) for dy in [-1, 0, 1] for dx in [-1, 0, 1] if (dx != 0 or dy != 0)]

    # for each co ord, check each direction at distance 4 (length of word xmas) and if xmas is made, increment the count
    # by true (1)
    for y, x in dict:
        for dy, dx in directions:
            candidate = "".join(dict.get((y + dy * i, x + dx * i), "") for i in range(4))
            count += candidate == "XMAS"
    print(count)

    # reset the count
    count = 0

    # for co ord in dict, if co ord is a, check each opposing corner to see if they match the MAS, only need M and S
    # as A is already in the middle
    for y, x in dict:
        if dict[y, x] == "A":
            lr = dict.get((y - 1, x - 1), "") + dict.get((y + 1, x + 1), "")
            rl = dict.get((y - 1, x + 1), "") + dict.get((y + 1, x - 1), "")
            count += {lr, rl} <= {"MS", "SM"}
    print(count)
