def has_overlap(a, b, complete = False):
    partial = a[0] >= b[0] and a[0] <= b[1]
    return partial and a[1] >= b[0] and a[1] <= b[1] if complete else partial

def check_line(line, complete = False):
    a, b = [[int(char) for char in pair.split('-')] for pair in line.split(',')]
    return 1 if has_overlap(a, b, complete) or has_overlap(b, a, complete) else 0

def ex1(input_path):
    with open(input_path, "r") as file:
        return sum([check_line(line, complete = True) for line in file.read().strip().split("\n")])

def ex2(input_path):
    with open(input_path, "r") as file:
        return sum([check_line(line, complete = False) for line in file.read().strip().split("\n")])

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
