import os
import re

MAX_PRESSES = 100

def get_max(button, p):
    return min(MAX_PRESSES, p//button)

def parse(line):
    return tuple([int(x) for x in re.findall("([0-9]+)",line)])

def get_cost(a, b, p):
    min_cost = None
    for sol in get_sol(a, b, p):
        cost = 3*sol[0]+sol[1]
        if not min_cost or cost < min_cost:
            min_cost = cost
    return min_cost

def diff(z):
    return z[1]-z[0]

def solution_is_valid(a, b, p, coeff_a, coeff_b):
    if a[0]*coeff_a+b[0]*coeff_b != p[0]: return False
    if a[1]*coeff_a+b[1]*coeff_b != p[1]: return False
    return True

def get_sol(a, b, p):
    solns = set()
    for coeff_a in range(MAX_PRESSES):
        rhs = diff(p)  - diff(a)*coeff_a
        coeff_b = rhs//diff(b)
        if not (rhs % diff(b) == 0): continue
        if not 0 <= coeff_b < MAX_PRESSES: continue
        if not solution_is_valid(a, b, p, coeff_a, coeff_b): continue
        solns.add((coeff_a, coeff_b))
    return solns

def main():
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        file_contents = f.readlines()
        num_machines = (len(file_contents)+1)//4
        cost = 0
        for m_index in range(num_machines):
            a = parse(file_contents[4*m_index])
            b = parse(file_contents[4*m_index+1])
            p = parse(file_contents[4*m_index+2])
            cost += get_cost(a, b, p) or 0
    print("Cost:", cost)
    print("Done")

main()