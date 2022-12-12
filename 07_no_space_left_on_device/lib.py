def parse_file(input_path):
    tree = {}
    stack = []
    with open(input_path, "r") as file:
        for line in file.read().splitlines():
            cwd = "/" + "/".join(stack)
            if line.startswith("$ cd"):
                if line.endswith(".."):
                    stack.pop()
                elif line.endswith("/"):
                    stack = []
                else:
                    _, __, dir = line.split(" ")
                    stack.append(dir)
            elif line.startswith("$ ls"):
                tree[cwd] = {}
            elif line[0].isdigit():
                size, name = line.split(" ")
                tree[cwd][name] = int(size)
    return tree

def sum_dir(tree, cwd):
    subdirs = filter(lambda path: path.startswith(cwd), tree.keys())
    return sum([sum(list(tree[path].values())) for path in subdirs])

def ex1(input_path):
    data = parse_file(input_path)
    total = 0
    for cwd in data.keys():
        dir_size = sum_dir(data, cwd)
        if dir_size <= 100_000:
            total += dir_size
    return total

def ex2(input_path):
    data = parse_file(input_path)
    total_space = 70_000_000
    required_space = 30_000_000
    used_space = sum_dir(data, "/")
    free_space = total_space - used_space
    space_delta = required_space - free_space
    totals = []
    for cwd in data.keys():
        dir_size = sum_dir(data, cwd)
        if dir_size > space_delta:
            totals.append((cwd, dir_size))
    totals.sort(key=lambda k: k[1])
    return totals[0][1]

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
