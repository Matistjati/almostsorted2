#!/usr/bin/python3

import sys
from random import randint
import random
import string
import math

n = random.randint(2, 10) # Very unlikely to be almost sorted at larger n


print(n)
print(" ".join(str(randint(1, n+5)) for i in range(n)))