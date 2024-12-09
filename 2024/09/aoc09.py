import math
import os

def get_checksum_delta(val, left_index, length):
    return sum([val * x for x in range(left_index, left_index + length)])

def get_index(val):
    return 2*(val)

def get_checksum_part_one(fs_rep):
    lhs_index = 0
    expanded_lhs_index = 0
    rhs_index = len(fs_rep) - 1
    checksum = 0
    lhs_file_val = 0
    rhs_file_val = int((len(fs_rep) - 1)/2)
    remaining_rhs = int(fs_rep[rhs_index])
    while (lhs_file_val < rhs_file_val):
        lhs_file_len = int(fs_rep[lhs_index])
        space_len = int(fs_rep[lhs_index + 1])
        # Count the non-spaces
        checksum += get_checksum_delta(lhs_file_val, expanded_lhs_index, lhs_file_len)
        lhs_file_val += 1
        expanded_lhs_index += lhs_file_len
        # Fill the spaces from the back
        while (space_len > 0 and rhs_index >= lhs_index + 2):
            gap_fill = min(remaining_rhs, space_len)
            checksum += get_checksum_delta(rhs_file_val, expanded_lhs_index, gap_fill)
            expanded_lhs_index += gap_fill
            remaining_rhs -= gap_fill
            space_len -= gap_fill
            if remaining_rhs == 0 and rhs_index >= lhs_index + 2:
                rhs_file_val -= 1 
                rhs_index -= 2 
                remaining_rhs = int(fs_rep[rhs_index])
        lhs_index += 2
    if (remaining_rhs > 0):
        checksum += get_checksum_delta(rhs_file_val, expanded_lhs_index, remaining_rhs)
    return checksum

def calc_moves(fs_rep):
    """Returns map of moved_val -> (start_index, length) """
    rhs_val = int((len(fs_rep) - 1)/2)
    used_spaces = {}
    moves = {}
    while (rhs_val > 0):
        len_rhs = int(fs_rep[get_index(rhs_val)])
        expanded_lhs_index = 0
        for lhs_val in range(rhs_val):
            expanded_lhs_index += int(fs_rep[get_index(lhs_val)]) 
            used_spaces.setdefault(lhs_val, 0)
            space_len = int(fs_rep[get_index(lhs_val) + 1]) - used_spaces[lhs_val]
            if (space_len >= len_rhs):
                moves[rhs_val] = (expanded_lhs_index + used_spaces[lhs_val], len_rhs)
                used_spaces[lhs_val] += len_rhs
                break
            expanded_lhs_index += int(fs_rep[get_index(lhs_val) + 1])
        rhs_val -= 1 
    return moves

def get_checksum_part_two(fs_rep):
    expanded_lhs_index = 0
    checksum = 0
    rhs_moved = calc_moves(fs_rep)
    for lhs_file_val in range(math.floor(len(fs_rep)/2)):
        lhs_file_len = int(fs_rep[get_index(lhs_file_val)])
        space_len = int(fs_rep[get_index(lhs_file_val) + 1])
        if (lhs_file_val not in rhs_moved):
            checksum += get_checksum_delta(lhs_file_val, expanded_lhs_index, lhs_file_len)
        expanded_lhs_index += lhs_file_len
        expanded_lhs_index += space_len
    for val, data in rhs_moved.items():
        # val -> (start_index, length) 
        checksum += get_checksum_delta(val, data[0], data[1])
    return checksum

def main():
    num_lines = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        fs_rep = f.readline().rstrip()
        checksum_part_one = get_checksum_part_one(fs_rep)
        checksum_part_two = get_checksum_part_two(fs_rep)
        print("Part one: ", checksum_part_one)
        print("Part two: ", checksum_part_two)
    print("Done")

main()