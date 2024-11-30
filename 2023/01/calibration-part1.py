import re
import os

total = 0


with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
    for line in f:
        digits = re.findall("[0-9]", line)
        calibration = 10*int(digits[0]) + int(digits[-1])
        total += calibration

print(total)