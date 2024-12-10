import os

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def step(pos, dir):
    return tuple(sum(x) for x in zip(pos, dir))

def reachable(from_pos):
    return [step(from_pos,dir) for dir in DIRS]

class Topo:
    def __init__(self):
        self._trailheads = set()
        self._summits = set()
        self._topo = []

    def in_bounds(self, pos):
        return ((0 <= pos[0] < len(self._topo[0])) and (0 <= pos[1] < len(self._topo)))
    
    def height_at(self, pos):
        return self._topo[pos[1]][pos[0]]
    
    def parse(self, line):
        self._topo += [[int(x) for x in line.rstrip()]]
        for index, el in enumerate(self._topo[-1]):
            if el == 0:
                self._trailheads.add((index,len(self._topo)-1))
            elif el == 9:
                self._summits.add((index,len(self._topo)-1))

    def steps_up(self, pos):
        next_steps = []
        height = self.height_at(pos)
        for new_pos in reachable(pos):
            if not (self.in_bounds(new_pos)): continue
            if (self.height_at(new_pos) - height) == 1:
                next_steps += [new_pos]
        return next_steps

    def score_trailheads(self, is_part_one):
        score = 0
        for th in self._trailheads:
            curr = [th]
            for ht in range(9):
                next = []
                for pos in curr:
                    next += self.steps_up(pos)
                curr = next
            if (is_part_one):
                score += len(set(curr))
            else:
                score += len(curr)
        return score

def main():
    topo = Topo()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            topo.parse(line)
    print("Part One score:", topo.score_trailheads(True))
    print("Part Two score:", topo.score_trailheads(False))
    print("Done")

main()