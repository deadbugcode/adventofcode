import os
from enum import Enum

class Letter(Enum):
    X = 0
    M = 1
    A = 2
    S = 3

class Puzzle:
    def __init__(self):
        self._letters = {}
        for l in Letter:
            self._letters[l.value] = set()
        self._num_rows = 0
        self._num_cols = 0

    def parse(self, row, row_num):
        self._num_cols = len(row.strip())
        self._num_rows = max(self._num_rows, row_num)
        for col_num in range(self._num_cols):
            self._letters[Letter[row[col_num]].value].add((col_num, row_num))
            
    def check(self, value, coordinates, direction):
        if coordinates not in self._letters[value]:
            # This direction doesn't have the full word.
            return False
        if (value == Letter.S.value):
            # Reached end of word.
            return True
        new_coordinates = tuple(map(sum, zip(coordinates, direction)))
        new_value = value + 1
        # Check next letter.
        return self.check(new_value, new_coordinates, direction)

    def part_one(self):
        num_true = 0
        for start_coordinates in self._letters[0]:
            for x_direction in range(-1, 2):
                for y_direction in range(-1, 2):
                    if x_direction == 0 and y_direction == 0:
                        continue
                    if self.check(0, start_coordinates, (x_direction, y_direction)):
                        num_true += 1
        return num_true
    
    def part_two(self):
        num_true = 0
        for start_coordinates in self._letters[1]:
            second_start = (start_coordinates[0] + 2, start_coordinates[1])
            if second_start in self._letters[1]:
                for y_direction in [-1, 1]:
                    if not self.check(1, start_coordinates, (1, y_direction)): continue
                    if self.check(1, second_start, (-1,y_direction)):
                        num_true += 1
            second_start = (start_coordinates[0], start_coordinates[1] + 2)
            if second_start in self._letters[1]:
                for x_direction in [-1, 1]:
                    if not self.check(1, start_coordinates, (x_direction, 1)): continue
                    if self.check(1, second_start, (x_direction, -1)):
                        num_true += 1
        return num_true

def main():
    p = Puzzle()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        line_num = 0
        for line in f:
            p.parse(line, line_num)
            line_num += 1
    print("Num XMAS:", p.part_one())
    print("Num X-MAS:", p.part_two())

main()