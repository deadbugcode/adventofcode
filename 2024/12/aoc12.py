from collections import deque
import os

DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def neighbours(pos):
    return [tuple(sum(x) for x in zip(pos, dir)) for dir in DIRS]

def neighbours_and_dirs(pos):
    return {tuple(sum(x) for x in zip(pos, dir)): dir for dir in DIRS}

def get_perimeter(all_pos):
    perimeter = 0
    for pos in all_pos:
        for neighbour in neighbours(pos):
            if neighbour not in all_pos:
                perimeter += 1
    return perimeter

def count_sides(all_pos):
    sides = 0
    border = {}
    for pos in sorted(all_pos):
        for n, d in neighbours_and_dirs(pos).items():
            if n in all_pos: continue
            border.setdefault(n, set())
            border[n].add(d)
            should_count = True
            for bn in neighbours(n):
                if bn in border and d in border[bn]:
                        should_count = False
                        break
            if should_count:
                sides += 1
    return sides

class Plot:
    def __init__(self):
        self._map = []
        self._groups = {}
    
    def height(self):
        return len(self._map)

    def width(self):
        return len(self._map[0])

    def plant_at(self, pos):
        return self._map[pos[1]][pos[0]]

    def get_contiguous(self, pos):
        n = []
        for dir in DIRS:
            new_pos = tuple(sum(x) for x in zip(pos, dir))
            if not 0 <= new_pos[0] < self.width(): continue
            if not 0 <= new_pos[1] < self.height(): continue
            if self.plant_at(pos) != self.plant_at(new_pos): continue
            n.append(new_pos)
        return n
    
    def get_all_contiguous(self, pos):
        visited = set()
        to_visit = deque([pos])
        while (len(to_visit) > 0):
            curr = to_visit.pop()
            for p in self.get_contiguous(curr):
                if p not in visited:
                    to_visit += [p]
            visited.add(curr)
        return visited
    
    def parse(self, line):
        self._map.append(list(line))


    def group(self):
        visited = set()
        for x in range(self.width()):
            for y in range(self.height()):
                if (x, y) in visited: continue
                self._groups[(x,y)] = self.get_all_contiguous((x,y))
                visited = visited.union(self._groups[(x,y)])
                
    def get_cost(self):
        cost = 0
        x_limits = {}
        y_limits = {}
        for group, points in self._groups.items():
            area = len(points)
            perimeter = get_perimeter(points)
            cost += area * perimeter
        return cost

    def get_discount_cost(self):
        cost = 0
        x_limits = {}
        y_limits = {}
        for group, points in self._groups.items():
            area = len(points)
            sides = count_sides(points)
            #print("Cost for ", self.plant_at(group), ":", area, "x", sides)
            cost += area * sides
        return cost
            
def main():
    num_lines = 0
    plot = Plot()
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            plot.parse(line.rstrip())
            num_lines += 1
    plot.group()
    print("Cost part 1:", plot.get_cost())
    print("Cost part 2:", plot.get_discount_cost()) 
    print("Done")

main()