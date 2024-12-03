import os
import re

def calculate(match):
    nums = match.group().split(',')
    first = int(nums[0][4:])
    second = int(nums[1][:len(nums[1])-1])
    return first * second

def part_one():
    mul_regex = re.compile('mul\([0-9]*\,[0-9]*\)')
    sum_mul = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            for match in mul_regex.finditer(line):
                sum_mul += calculate(match)
    print("Sum of mul", sum_mul)


def part_two():
    cond_regex = re.compile('do(n\'t)?\(\)')
    mul_regex = re.compile('mul\([0-9]*\,[0-9]*\)')
    sum_mul = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        enabled = True
        for line in f:
            for i in range(len(line)):
                cond_match = cond_regex.match(line[i:])
                mul_match = mul_regex.match(line[i:])
                if cond_match is not None:
                    enabled = (cond_match.span()[1] - cond_match.span()[0] <= 4) # Is it a do()
                if enabled and mul_match is not None:
                    sum_mul += calculate(mul_match)
    print("Sum of Mul with don'ts", sum_mul)


def main():
    part_one()
    part_two()

main()