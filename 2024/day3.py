import re


def enable():
    global enabled
    enabled = 1


def disable():
    global enabled
    enabled = 0


def mul(x, y):
    global total, enabled
    if enabled:
        total += x * y


with open('in.txt') as inp:
    inp = inp.read()
    enabled = 1

    # part 1
    total = 0
    regex = r"mul\(\d+,\d+\)"
    f = re.findall(regex, inp)
    list(map(exec, f))
    print(total)

    # part 2
    total = 0
    regex2 = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    f = re.findall(regex2, inp)
    list(map(lambda s: exec(s.replace('don\'t', 'disable').replace("do", 'enable')), f))
    print(total)
