import os
import sys
from collections import defaultdict, deque, Counter
def part_2(data):
    G = defaultdict(int)
    s = 0
    for i, line in enumerate(data):
        G[i] += 1
        card, item = line.split('|')
        id, split = card.split(':')
        splits = [int(x) for x in split.split()]
        items = [int(x) for x in item.split()]
        val = len(set(splits) & set(items))
        if val > 0:
            s += 2 ** (val - 1)

        for j in range(val):
            G[i + 1 + j] += G[i]
    print(sum(G.values()))


def part_1(data):
    G = defaultdict(int)
    s = 0
    for i, line in enumerate(data):
        G[i] += 1
        card, item = line.split('|')
        id, split = card.split(':')
        splits = [int(x) for x in split.split()]
        items = [int(x) for x in item.split()]
        val = len(set(splits) & set(items))
        if val > 0:
            s += 2**(val-1)

        for j in range(val):
            G[i+1+j] += G[i]
    print(s)



def parse(d):
    return d.split('\n')


with open('inputs.txt', 'r') as fh:
    d = fh.read().strip()
    data = parse(d)

    part_1(data)
    part_2(data)