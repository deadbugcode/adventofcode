import os

def is_lock(block):
    return '.' not in block[0]

def parse_lock(block):
    out = [0] * 5
    for i in range(5):
        for j in range(6):
            if block[1+j][i] == '.':
                out[i] = j
                break
    return out

def parse_key(block):
    out = [5] * 5
    for i in range(5):
        for j in range(6):
            if block[1+j][i] == '#':
                out[i] = 5-j
                break
    return out

def fits(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 5: return False
    return True

def main():
    num_lines = 0
    locks = []
    keys = []
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        lines = f.readlines()
        num_blocks = (len(lines) + 1) // 8
        for i in range(num_blocks):
            block = [list(l.rstrip()) for l in lines[i*8: i*8+7]]
            if (is_lock(block)):
                locks += [parse_lock(block)]
            else:
                keys += [parse_key(block)]

    count = 0
    for k in keys:
        for l in locks:
            if fits(k,l):
                count += 1
    print("part one:", count)
    # TODO: Finish the other days, get to access part 2
    print("Done")

main()