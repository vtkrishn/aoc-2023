import os
import sys
from collections import defaultdict, deque, Counter

def part_2(data):
    p2 = 0
    for i in data:
        _id, line = i.split(':')
        m = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                m[color] = max(m[color], int(n))
        score = 1
        for v in m.values():
            score *= v
        p2 += score
    print(p2)

def part_1(data):
    p1 = 0
    for i in data:
        ok = True
        id_, line = i.split(':')
        V = defaultdict(int)
        for event in line.split(';'):
            for balls in event.split(','):
                n, color = balls.split()
                n = int(n)
                V[color] = max(V[color], n)
                if int(n) > {'red': 12, 'green': 13, 'blue': 14}.get(color, 0):
                    ok = False
        if ok:
            p1 += int(id_.split()[-1])
    print(p1)


def parse(data):
    return data


with open('inputs.txt', 'r') as fh:
    d = fh.read().strip()
    d = d.split('\n')
    data = parse(d)

    part_1(data)
    part_2(data)
