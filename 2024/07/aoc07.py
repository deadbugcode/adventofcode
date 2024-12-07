import os


def concat(a, b):
    return int(str(a)+str(b))

def check_combo(lhs, rhs, index, res):
    if res > lhs:
        return False
    if index == len(rhs):
        #print(lhs, res, lhs == res)
        return res == lhs
    if check_combo(lhs, rhs, index + 1, res * rhs[index]):
        return True
    if check_combo(lhs, rhs, index + 1, res + rhs[index]):
        return True
    # For part 2:
    return check_combo(lhs, rhs, index + 1, concat(res, rhs[index]))

def combo_exists(lhs, rhs):
    if (len(rhs)) == 1:
        return lhs == rhs
    return check_combo(lhs, rhs, 1, rhs[0])

def main():
    total = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            (lhs, rhs) = line.rstrip().split(':', 1)
            lhs = int(lhs)
            rhs = [int(x) for x in rhs.strip().split()]
            if (combo_exists(lhs, rhs)):
                total += lhs
    print("Result: ", part_one_total)

main()