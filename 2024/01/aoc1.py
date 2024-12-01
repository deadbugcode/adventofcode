import math
import os

# This doesn't work because I forgot how to do this properly, obviously
def insert_sorted(element, sorted_list):
    idx = math.floor(len(sorted_list) / 2)
    while (idx > 0 and idx < len(sorted_list)):
        el_gt_left = element > sorted_list[idx - 1]
        el_gt_right = element > sorted_list[idx]
        diff = 0
        if (el_gt_left and el_gt_right):
            diff = (math.floor( (len(sorted_list) - 1 - idx) / 2 + 1))
        elif (not el_gt_right and not el_gt_left):
            diff = - math.floor((idx + 1)/2)
        if (diff == 0): break
    sorted_list.insert(idx, element)

def part_one():
    list1 = []
    list2 = []  
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            inputs = line.strip().split()
            print(inputs)
            #insert_sorted(int(inputs[0]), list1)
            #insert_sorted(int(inputs[1]), list2)
            list1.append(int(inputs[0]))
            list2.append(int(inputs[1]))

    list1.sort()
    list2.sort()
    distancediff = 0
    if (len(list1) != len(list2)):
        print("List length error")
        return
    for idx in range(len(list1)):
        distancediff += abs(list1[idx] - list2[idx])
    print("Part 1 - distance diff:", distancediff)


def get_count_or_zero(key, dictionary):
    if (key not in dictionary): return 0
    return dictionary[key]

def part_two():
    list1 = {}
    list2 = {}
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            inputs = line.strip().split()
            list1[int(inputs[0])] = get_count_or_zero(int(inputs[0]), list1) + 1
            list2[int(inputs[1])] = get_count_or_zero(int(inputs[1]), list2) + 1
    similarity = 0
    for key in list1.keys():
        lhs_count = get_count_or_zero(key, list1)
        rhs_count = get_count_or_zero(key, list2)
        similarity += lhs_count * rhs_count * key
    print("Part 2 - similarity:", similarity)
    

def main():
    part_one()
    part_two()

main()