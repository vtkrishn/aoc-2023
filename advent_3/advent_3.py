import os
import sys
from collections import defaultdict, deque, Counter
def part_2(data):
    D = [[c for c in l] for l in data]
    m = len(data)
    n = len(data[0])
    s = 0
    nums = defaultdict(list)
    for i in range(m):
        st = set()
        val = 0
        has_part = False
        for j in range(n + 1):
            if j < n and D[i][j].isdigit():
                val = val * 10 + int(D[i][j])
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        if 0 <= i + rr < m and 0 <= j + cc < n:
                            d = D[i + rr][j + cc]
                            if not d.isdigit() and d != '.':
                                has_part = True
                            if d == '*':
                                st.add((i+rr, j+cc))
            elif val > 0:
                for t in st:
                    nums[t].append(val)
                val = 0
                st = set()
    for k,v in nums.items():
      if len(v)==2:
        s += v[0]*v[1]
    print(s)


def part_1(data):
    D = [[c for c in l] for l in data]
    m = len(data)
    n = len(data[0])
    s = 0
    for i in range(m):
        val = 0
        has_part = False
        for j in range(n+1):
            if j < n and D[i][j].isdigit():
                val = val * 10 + int(D[i][j])
                for rr in [-1,0,1]:
                    for cc in [-1,0,1]:
                        if 0<=i+rr<m and 0<=j+cc<n:
                            d = D[i+rr][j+cc]
                            if not d.isdigit() and d != '.':
                                has_part = True
            elif val > 0:
                if has_part:
                    s += val
                val = 0
                has_part = False
    print(s)



def parse(d):
    return d.split('\n')


with open('inputs.txt', 'r') as fh:
    d = fh.read().strip()
    data = parse(d)

    part_1(data)
    part_2(data)
