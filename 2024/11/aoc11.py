import os
import math

def blink(stone):
    # Slower
    if (int(stone) == 0):
        return ["1"]
    elif ((len(stone)) % 2 == 0):
        mid = int(len(stone)/2)
        return [str(int(stone[:mid])), str(int(stone[mid:]))]
    return [str(int(stone)*2024)]

def blink_int(stone):
    # Faster, but doesn't change much
    if (stone == 0):
        return [1]
    num_digits = int(math.log10(stone)) + 1
    if (num_digits % 2 == 0):
        halfway = math.pow(10,int(num_digits/2))
        return [int(stone/halfway), int(stone % halfway)]
    return [stone*2024]

def count_stones(stone, num_blinks):
    # Works for part one, too slow for part 2
    stones = [stone]
    for _ in range(num_blinks):
        next_stones =  []
        for s in stones:
            next_stones += blink_int(s)
        stones = next_stones
    return len(stones)

def count_stones_collapse(stone, num_blinks):
    stones = {stone: 1}
    for _ in range(num_blinks):
        next_stones =  {}
        for (s, count) in stones.items():
            for new_s in blink_int(s):
                next_stones.setdefault(new_s, 0)
                next_stones[new_s] += count
        stones = next_stones
    return sum(stones.values())

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        l = f.readline()
        total_stones = 0
        for stone in l.rstrip().split(' '):
            total_stones += count_stones_collapse(int(stone), 75)
        print("Num stones:", total_stones)
    print("Done")

main()