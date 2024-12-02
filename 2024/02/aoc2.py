import os

def is_safe(values):
    is_safe = True
    is_increasing = int(values[1]) >= int(values[0])
    for i in range(1, len(values)):
        if ((int(values[i]) >= int(values[i-1])) != is_increasing):
            is_safe = False
            break
        diff = abs(int(values[i]) - int(values[i-1]))
        if (diff > 3 or diff < 1):
            is_safe = False
            break
    return is_safe    

def safe_without_index(values, index):
    removed = [] 
    if (index == 0):
        removed = values[1:]
    elif (index == len(values)):
        removed = values[:index - 1]
    else:
        removed = values[:index] + values[index + 1:]
    return is_safe(removed)

def part_one():
    num_safe_reports = 0
    num_lines = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            num_lines += 1
            report = line.strip().split()
            if (is_safe(report)):
                num_safe_reports +=1
            
    print("Safe reports: ", num_safe_reports, " of ", num_lines)

def part_two():
    num_safe_reports = 0
    num_lines = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt"),"r") as f:
        for line in f:
            num_lines += 1
            report = line.strip().split()
            if (is_safe(report)):
                num_safe_reports += 1
                continue
            for i in range(len(report)):
                if(safe_without_index(report, i)):
                    num_safe_reports += 1
                    break
    print("Safe reports with 1 bad level: ", num_safe_reports, " of ", num_lines)

def main():
    part_one()
    part_two()   

main()