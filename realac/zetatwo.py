#!/usr/bin/env python3

n = int(input())
numbers = [int(x) for x in input().split()]

def debug_print(*args, **kwargs):
    if False:
        print(*args, **kwargs)

# Find candidate sub-array
i = None
j = None
fail = False
for cur_idx in range(1, n):
    cur = numbers[cur_idx]
    prev = numbers[cur_idx-1]

    # Found first down slope
    if cur < prev and i == None:
        i = cur_idx-1
    
    # Found up slope again
    if cur > prev and i != None and j == None:
        j = cur_idx


# Down slope went to the end
if j == None:
    j = n


# Start counting up
# If we have found a down slope, first count up in the up slope before it (potentially len=0)
prev = None
debug_print(i, j)
if i:
    debug_print('Up')
    for part1_idx in range(i):
        cur = numbers[part1_idx]
        debug_print(f'{part1_idx}: {prev} <?> {cur}')
        if prev and prev > cur:
            fail = True
        prev = cur

# Then count up backwards in the down slope
if i:
    debug_print('Down')
    for part2_idx in range(j-1, i-1, -1):
        cur = numbers[part2_idx]
        debug_print(f'{part2_idx}: {prev} <?> {cur}')
        if prev and prev > cur:
            fail = True
        prev = cur

# Then finally if there is another up slope, keep counting up
debug_print('Up')
for part3_idx in range(j, n):
    cur = numbers[part3_idx]
    debug_print(f'{part3_idx}: {prev} <?> {cur}')
    if prev and prev > cur:
        fail = True
    prev = cur

# Did we at any point fail to keep counting upwards?
if fail:
    print('No')
else:
    print('Yes')
