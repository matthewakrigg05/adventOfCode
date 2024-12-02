def checkSafe(report):
    incr = False
    decr = False
    isSafe = 0

    for i in range(len(report) - 1):
        isSafe = 1
        diff = report[i + 1] - report[i]

        if not 0 < (abs(diff)) < 4:
            isSafe = 0
            break
        if diff > 0:
            incr = True
        if diff < 0:
            decr = True
        if incr is True and decr is True:
            isSafe = 0
            break

    return isSafe


with open('in.txt', 'r') as f:
    count = 0
    for report in f:
        report = [int(level) for level in report.split()]
        incr = False
        decr = False
        safe = checkSafe(report)
        if safe == 0:
            for i in range(len(report)):
                temp = report.pop(i)
                safe = checkSafe(report)
                if safe == 1:
                    break
                report.insert(i, temp)
        count += safe

    print(count)
