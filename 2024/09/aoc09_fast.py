import math
import os

def get_checksum_delta(val, left_index, length):
    return sum([val * x for x in range(left_index, left_index + length)])

def get_index(val):
    return 2*(val)

def calc_moves(fs_rep):
    """Returns map of moved_val -> (start_index, length) """
    # Optimization 1: only do the string->int conversion once
    fs_rep_int = [int(fs_rep[x]) for x in range(len(fs_rep))]
    # Optimization 2: pre-calculate expanded indices once
    expanded_indices = [fs_rep_int[0]] + [0] * (len(fs_rep_int) - 1)
    for i in range(len(fs_rep_int)):
        expanded_indices[i] = expanded_indices[i-1] + fs_rep_int[i]
    rhs_val = int((len(fs_rep) - 1)/2)
    used_spaces = {}
    moves = {}
    while (rhs_val > 0):
        len_rhs = fs_rep_int[get_index(rhs_val)]
        for lhs_val in range(rhs_val):
            used_spaces.setdefault(lhs_val, 0)
            space_len = fs_rep_int[get_index(lhs_val) + 1] - used_spaces[lhs_val]
            if (space_len >= len_rhs):
                moves[rhs_val] = (expanded_indices[get_index(lhs_val)] + used_spaces[lhs_val], len_rhs)
                used_spaces[lhs_val] += len_rhs
                break
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
        checksum_part_two = get_checksum_part_two(fs_rep)
        print("Part two: ", checksum_part_two)
    print("Done")

main()