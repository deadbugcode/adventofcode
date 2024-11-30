import os

_DIGITS = {
    'one': 1, 
    'two': 2, 
    'three': 3, 
    'four': 4, 
    'five': 5, 
    'six': 6, 
    'seven': 7, 
    'eight': 8, 
    'nine': 9
    }


def getdigit(line, index):
    if line[index].isdigit():
        return int(line[index])
    for digit in _DIGITS.keys():
        if (line[index:]).startswith(digit):
            return _DIGITS[digit]
    return 0


# Part 2.
def main():
    total = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input2.txt"),"r") as f:
        for line in f:
            first = 0
            last = 0
            for i in range(len(line)-1):
                first = getdigit(line, i)
                if first != 0:
                    break
            for i in range(len(line)-1,-1, -1):
                last = getdigit(line, i)
                if last != 0:
                    break
            calibration = 10*first + last
            total += calibration
    print(total)

main()