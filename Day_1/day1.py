import re

# read input file
file = open('./input.txt').read()

# Set vars
total = 0
result = 0

for line in file.split('\n'):
    digits = []

    for val in line:
        if val.isdigit():
            digits.append(val)
    
    total = int(digits[0]+digits[-1])
    result += total

print('Part 1:', result)

# Reset variables
result = 0
total = 0

for line in file.split('\n'): 
    digits = []
    
    for num,val in enumerate(line):
        if val.isdigit():
            digits.append(val)
        for d,val in enumerate(['one','two','three','four','five','six','seven','eight','nine']):
            if line[num:].startswith(val):
                digits.append(str(d+1))
    total = int(digits[0]+digits[-1])
    result += total

print('Part 2:', result)