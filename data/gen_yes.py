#!/usr/bin/python3

import sys
from random import randint
import random
import string
import math

n = random.randint(2, 10)
arr = sorted(random.randint(1, n//2) for _ in range(n))
start, end = random.randint(0, n - 1), random.randint(0, n - 1)
start, end = min(start, end), max(start, end)
arr[start:end] = reversed(arr[start:end])

print(n)
print(" ".join(map(str, arr)))