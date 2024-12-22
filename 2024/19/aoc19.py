import os

# Patterns preprocessed in vi with
# :s/\, /\"\, \"/g
PATTERNS = ["r", "wr", "b", "g", "bwu", "rb", "gb", "br"] # Example
# Input patterns var omitted because everyone's input is different.

def check(pieces):
    if (len(pieces)==0):
        return True
    for n in pieces[0]:
        if n <= len(pieces) and check(pieces[n:]): return True
    return False

def possible(design):
    pieces = preprocess(design)
    return check(pieces)

def preprocess(design):
    # Set only works for part 1
    # pieces = [set() for _ in range(len(design))]
    pieces = [list() for _ in range(len(design))]
    for i in range(len(design)):
        for p in PATTERNS:
            if design[i:i+len(p)] == p:
                pieces[i] += [len(p)]
    return pieces

def count_combos(pieces):
    # Recursive is too slow for part 2
    if len(pieces) == 0: return 0
    counts = [1] + [0] * (len(pieces))
    for index in range(len(pieces)):
        if counts[index] == 0: continue
        for n in pieces[index]:
            if n <= len(pieces) - index:
                counts[index + n] += counts[index]
    return counts[-1]

def get_num_combos(design):
    pieces = preprocess(design)
    return count_combos(pieces)


def main():
    count = 0
    combos = 0
    # File contains only the desired designs.
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            design = line.rstrip()
            if(possible(design)): 
                count+=1
            num = get_num_combos(design)
            combos += num

    print("[Part 1] Num possible designs:", count)
    print("[Part 2] Num combos:", combos)

main()