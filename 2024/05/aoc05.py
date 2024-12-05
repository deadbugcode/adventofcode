import math
import os

class Rules:
    def __init__(self):
        self._rule_map = {}

    # Internal use only
    def insert_one(self, key, pair):
        if key not in self._rule_map: 
            self._rule_map[key] = set()
        self._rule_map[key].add(pair)

    def insert(self, pair):
        self.insert_one(pair[0], tuple(pair))
        self.insert_one(pair[1], tuple(pair))

    def contains(self, pair):
        return pair in (self._rule_map[pair[0]] or [])
    
    def parse_pair(self, pair_str):
        pair = pair_str.rstrip().split("|", 1)
        if len(pair) < 2: 
            return False
        self.insert(pair)
        return True

    def build(self):
        # Which turned out to be unnecessary, in the end.
        num_nodes_added = 0
        for key, pairs in self._rule_map.items():
            for pair in pairs:
                # No double-counting
                if pair[1] == key: continue
                second_key = pair[1]
                for second_pair in self._rule_map[second_key] or set():
                    # No double-counting
                    if second_pair[1] == second_key: continue
                    if self.contains((key, second_pair[1])): continue
                    self.insert(key, second_pair[1])
                    num_nodes_added += 1
        if num_nodes_added > 0:
            self.build()
    
    def page_compare(self, lhs, rhs):
        if rhs not in self._rule_map:
            return 0
        for a, b in self._rule_map.get(lhs) or []:
            if a == rhs: return 1 # lhs > rhs
            if b == rhs: return -1 # lhs < rhs
        # No comparison found
        return 0

    def next_index_in_rulemap(self, start_index, values):
        if start_index == -1 or start_index >= len(values):
            return -1
        for index in range(start_index,len(values)):
            if values[index] in self._rule_map:
                return index
        return -1


def part_one(rules, updates):
    sum_middle_pages = 0
    for u in updates:
        bad_update = False
        for index, page in enumerate(u):
            for other_index in range(index + 1, len(u)):
                if (rules.page_compare(page, u[other_index])) == 1:
                    #print(page, "is gt", u[other_index])
                    bad_update = True
                    break
            if (bad_update):
                break
        if not bad_update:
            sum_middle_pages += int(u[math.ceil((len(u) - 1)/2)])
    print(sum_middle_pages)


def part_two(rules, updates):
    sum_middle_pages = 0
    for u in updates:
        bad_update = False
        for index in range(len(u)):
            for other_index in range(index + 1, len(u)):
                if (rules.page_compare(u[index], u[other_index])) == 1:
                    bad_update = True
                    u[index], u[other_index] = u[other_index], u[index]
        if bad_update:
            sum_middle_pages += int(u[math.ceil((len(u) - 1)/2)])
    print(sum_middle_pages)

def main():
    r = Rules()
    updates = []
    rules_complete = False
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            if rules_complete:
                if len(line.rstrip()) > 0:
                    updates.append(line.rstrip().split(","))
            # Otherwise, continue parsing the rules.
            elif not r.parse_pair(line):
                rules_complete = True
    # r.build()
    part_one(r, updates)
    part_two(r, updates)
    print("Done")

main()