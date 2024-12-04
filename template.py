import os

def main():
    num_lines = 0
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "example.txt"),"r") as f:
        for line in f:
            num_lines += 1
    print("Done")

main()