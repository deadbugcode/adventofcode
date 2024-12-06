import os

GUARD_CHARS = {
    '^' : (-1, 0),
    '>': (0, 1),
    '<': (-1, 0),
    'v': (0, -1),
}

def turn_90_deg(dir):
    match(dir):
        case((-1, 0)):
            return (0, 1)
        case((0, 1)):
            return (1, 0)
        case((1, 0)):
            return (0, -1)
        case((0, -1)):
            return (-1, 0)
    return None

class Map:
    def __init__(self):
        self._obstacles = set()
        self._guard_pos = (-1, -1)
        self._guard_dir = (0, 0)
        self._guard_pos_dir = {}
        
        self._horizontal_wall = 0
        self._vertical_wall = 0

    def parse(self, row, row_num):
        self._horizontal_wall = len(row)
        self._vertical_wall = row_num + 1
        for col_num, val in enumerate(row):
            if val == '#':
                self._obstacles.add((row_num, col_num))
            elif val in GUARD_CHARS.keys():
                self._guard_pos = (row_num, col_num)
                self._guard_dir = GUARD_CHARS[val]
    
    
    def guard_is_outside(self):
        if (self._guard_pos[0] < 0 or self._guard_pos[0] >= self._horizontal_wall):
            return True
        if (self._guard_pos[1] < 0 or self._guard_pos[1] >= self._vertical_wall):
            return True
        return False

    def gen_guard_path(self):
        while (not self.guard_is_outside()):
            if self._guard_pos in self._guard_pos_dir:
                if self._guard_dir in self._guard_pos_dir[self._guard_pos]:
                    # We've been here before.
                    return
                else:
                    self._guard_pos_dir[self._guard_pos].add(self._guard_dir)
            else:
                self._guard_pos_dir[self._guard_pos] = set([self._guard_dir])
            # Go forward
            next_pos =tuple(sum(x) for x in zip(self._guard_pos, self._guard_dir))
            if (next_pos in self._obstacles):
                # Change direction & try again
                self._guard_dir = turn_90_deg(self._guard_dir)
                continue
            # Move
            self._guard_pos = next_pos

    def count_guard_positions(self):
        self.gen_guard_path()
        return (len(self._guard_pos_dir.keys()))
    

def main():
    num_lines = 0
    m = Map()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"), "r") as f:
        for line in f:
            m.parse(line, num_lines)
            num_lines += 1
    print("Part one:", m.count_guard_positions())

main()