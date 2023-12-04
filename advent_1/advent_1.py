import os
import sys
import re
from collections import defaultdict, deque, Counter
def part_2(data):
    #print(data)
    s = 0
    for i in data:
        d = []
        for j, c in enumerate(i):
            if c.isdigit():
                d.append(c)
            for k, val in enumerate(['zero','one','two','three','four','five','six','seven','eight','nine']):
                if i[j:].startswith(val):
                    d.append(str(k))
        s += int(d[0] + d[-1])
    print(s)

def part_1(data):
    #print(data)
    s = 0
    for i in data:
        d = []
        for j, c in enumerate(i):
            if c.isdigit():
                d.append(c)
        s += int(d[0] + d[-1])
    print(s)

def parse(data):
    return data


with open('inputs.txt', 'r') as fh:
    d = fh.read().splitlines()
    data = parse(d)

    part_1(data)
    part_2(data)