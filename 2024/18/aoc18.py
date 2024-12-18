import os
import re

#SIZE = 6 # Example
#NUM_STEPS = 12 # Example

SIZE = 70 # Input
NUM_STEPS = 1024 # Input

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def neighbours(pos):
    return [tuple(sum(x) for x in zip(pos, dir)) for dir in DIRS]

class Map:
    def __init__(self, size, num_steps):
        self._size = size
        self._num_steps = num_steps
        # Map of obstacles to the time they appeared
        self._obstacles = {}

    def parse(self, line, line_num):
        coords = tuple([int(x) for x in re.findall("([0-9]+)",line)])
        self._obstacles[coords] = line_num

    def has_obstacle_at(self, pos, time):
        if pos not in self._obstacles: return False
        return self._obstacles[pos] <= time

    def has_obstacle(self, pos):
        return self.has_obstacle_at(pos, self._num_steps)

    def shortest_exit_path(self):
        return self.shortest_exit_path_at(self._num_steps)

    def shortest_exit_path_at(self, time):
        curr = set([(0,0)])
        num_steps = 0
        visited = set()
        while((self._size, self._size) not in curr):
            next_steps = set()
            if len(curr) == 0: return None
            for c in curr:
                for n in neighbours(c):
                    if not 0 <= n[0] <= self._size: continue # X OOB
                    if not 0 <= n[1] <= self._size: continue # Y OOB
                    if n in visited: continue # No retracing steps
                    if self.has_obstacle_at(n, time): continue # Blocked
                    next_steps.add(n)
            curr = next_steps
            visited = visited.union(curr)
            num_steps += 1
        return num_steps

    def get_block_at(self, time):
        for o,t in self._obstacles.items():
            if t == time: return o
        return None

    def get_blocking_block(self):
        min_t = self._num_steps # As we know from part one.
        max_t = len(self._obstacles)
        while (min_t + 1 < max_t): 
            t = (max_t + 1 - min_t) // 2 + min_t
            if (self.shortest_exit_path_at(t) is None):
                max_t = t
            else:
                min_t = t
        return self.get_block_at(max_t)

def main():
    num_lines = 0
    map = Map(SIZE, NUM_STEPS)
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line_num, line in enumerate(f.readlines()):
            map.parse(line.rstrip(), line_num+1)
    print("Part one:", map.shortest_exit_path())
    print("Part two:", map.get_blocking_block())
    print("Done")

main()