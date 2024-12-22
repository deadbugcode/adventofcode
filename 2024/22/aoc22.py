import re
import os

BANANA_COUNT= {}

def parse(line):
    return ([int(x) for x in re.findall("([0-9]+)",line.rstrip())])[0]

def next_secret_num(n):
    next_sn = n
    step1 = bin(next_sn) + "000000" # x64
    next_sn = mix_and_prune(next_sn, step1)

    step2 = bin(0)
    if (next_sn >= 32):
        step2 = bin(next_sn)[:-5] # //32
    next_sn = mix_and_prune(next_sn, step2)
    
    step3 = bin(next_sn) + "00000000000" # x 2048  (2^11)
    next_sn = mix_and_prune(next_sn, step3)
    return next_sn

def mix_and_prune(sn, val_str):
    # Prune first, order of op doesn't matter
    pruned_val = 0
    if len(val_str) > 25:
        pruned_val = int(val_str[len(val_str)-24:],2)
    else:
        pruned_val = int(val_str, 2)
    mix = sn ^ pruned_val
    return mix

def nth_sn(start, nth):
    # Part one.
    curr = start
    for _ in range(nth):
        curr = next_secret_num(curr)
    return curr

def process(start, nth):
    # Parts one & two.
    curr = start
    prices = []
    for _ in range(nth):
        prices += [curr % 10]
        curr = next_secret_num(curr)
    max_banana(prices)
    return curr

def gen_diffs(prices):
    diffs = [0] * (len(prices) - 1)
    for i in range(1,len(prices)):
        diffs[i-1] = prices[i]-prices[i-1]
    return diffs

def max_banana(prices):
    diffs = gen_diffs(prices)
    seen_keys = set()
    for i in range(4,len(prices)):
        key = str(diffs[i-4:i])
        if key in seen_keys: continue
        seen_keys.add(key)
        BANANA_COUNT.setdefault(key, 0)
        BANANA_COUNT[key] += prices[i]

def test():
    sn = 123
    expected = [15887950, 16495136, 527345, 704524, 1553684, 12683156, 11100544, 12249484, 7753432, 5908254]
    expected_part2 = [-3, 6, -1, -1, 0, 2, -2, 0, -2]
    for i in range(len(expected)):
        sn = next_secret_num(sn)
        if sn != expected[i]:
            print("Failed case", i)
            print("Expected", expected[i], ", got", sn)        
            break
    prices = gen_prices(123,10)
    diffs = gen_diffs(prices)
    print(prices)
    print(diffs)
    for i in range(len(expected_part2)):
        if diffs[i] != expected_part2[i]:
            print("Failed case", i)
            print("Expected", expected_part2[i], ", got", diffs[i])        
            break
    
    print("All tests pass")


def main():
    sum = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            num = parse(line)
            nthnum = process(num, 2000)
            sum += nthnum
            
    print("Part one:", sum)
    print("Part two:", sorted(BANANA_COUNT.items(), key=lambda i: i[1])[-1][1])

    


main()