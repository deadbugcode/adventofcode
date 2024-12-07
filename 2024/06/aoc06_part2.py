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

def step(pos, dir):
    return tuple(sum(x) for x in zip(pos, dir))

def maybe_add_visited(curr_pos, curr_dir, visited_pos_and_dir):
    if curr_pos in visited_pos_and_dir:
        if curr_dir in visited_pos_and_dir[curr_pos]:
            # Not adding -- already exists
            return False
        else:
            visited_pos_and_dir[curr_pos].add(curr_dir)
    else:
        visited_pos_and_dir[curr_pos] = set([curr_dir])
    # Added
    return True

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
    
    def is_outside(self, pos):
        if (pos[0] < 0 or pos[0] >= self._horizontal_wall):
            return True
        if (pos[1] < 0 or pos[1] >= self._vertical_wall):
            return True
        return False

    def guard_is_outside(self):
        return self.is_outside(self._guard_pos)

    def validate_obstruction(self, new_obstruction):
        if self.is_outside(new_obstruction):
            return False
        if (new_obstruction in self._obstacles):
            return False
        return True

    def gen_guard_path(self):
        pos = self._guard_pos
        dir = self._guard_dir
        while (not self.is_outside(pos)):
            if not maybe_add_visited(pos, dir, self._guard_pos_dir):
                # Cycle detected, we're done.
                return
            next_pos = step(pos, dir)
            if (next_pos in self._obstacles):
                dir = turn_90_deg(dir)
                continue
            pos = next_pos

    def has_cycle(self, start_pos, start_dir, new_obstacle):
        pos = start_pos
        dir = start_dir
        visited = {}
        while (True):
            if self.is_outside(pos):
                return False
            if not maybe_add_visited(pos, dir, visited):
                return True
            # Go forward
            next_pos = step(pos, dir)
            if (next_pos in self._obstacles or next_pos == new_obstacle):
                # Change direction & try again
                dir = turn_90_deg(dir)
                continue
            # Move
            pos = next_pos
     
    def count_guard_positions(self):
        return (len(self._guard_pos_dir.keys()))       

    def count_possible_obstructions(self):
        obstructions = set()
        for pos, dirs in self._guard_pos_dir.items():
            for dir in dirs:
                new_obstruction = step(pos, dir)
                if new_obstruction in obstructions:
                    continue
                if not self.validate_obstruction(new_obstruction):
                    continue
                if self.has_cycle(self._guard_pos, self._guard_dir, new_obstruction):
                    obstructions.add(new_obstruction)
        return len(obstructions)


def main():
    num_lines = 0
    m = Map()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            m.parse(line, num_lines)
            num_lines += 1
    m.gen_guard_path()
    print("Part one:", m.count_guard_positions())
    print("Part two:", m.count_possible_obstructions())

main()