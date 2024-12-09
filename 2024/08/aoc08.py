import os

class AntennaMap:
    def __init__(self):
        self._antennas = {}
        self._antinodes = set()
        self._num_rows = 0 # y
        self._num_cols = 0 # x
    
    def set_dims(self, max_rows, max_cols):
        self._num_rows = max_rows
        self._num_cols = max_cols
    
    def parse(self, row, row_num):
        for col_num, val in enumerate(row):
            if (val == '.'):
                continue
            self._antennas.setdefault(val, set())
            new_antenna = (col_num, row_num)
            for other in self._antennas[val]:
                self.add_antinode_part_two(new_antenna, other)
                self.add_antinode_part_two(other, new_antenna)
            self._antennas[val].add(new_antenna)
            
    def add_antinode(self, first, second):
        self.maybe_add_antinode((2*second[0]- first[0], 2*second[1]-first[1]))
        self.maybe_add_antinode((2*first[0]- second[0], 2*first[1]-second[1]))

    def add_antinode_part_two(self, first, second):
        i = 1
        while(True):
            next_antinode = (i*second[0]-(i-1)*first[0], i*second[1]-(i-1)*first[1])
            print(i)
            print(next_antinode)
            if not self.maybe_add_antinode(next_antinode):
                break
            i += 1
        

    def maybe_add_antinode(self, point):
        should_add = self.space_is_available(point)
        if should_add:
            self._antinodes.add(point)
        return should_add

    def space_is_available(self, point):
        if not (0 <= point[0] < self._num_cols):
            return False # Out of bounds x-axis
        if not (0 <= point[1] < self._num_rows):
            return False # Out of bounds y-axis
        return True
        

def main():
    am = AntennaMap()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        lines = f.readlines()
        am.set_dims(len(lines[0].rstrip()), len(lines))
        for num_lines, line in enumerate(lines):
            am.parse(line.rstrip(), num_lines)
    print((am._antinodes))
    print(len(am._antinodes))

main()