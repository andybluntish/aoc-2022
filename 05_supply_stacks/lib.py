def parse_file(input_path):
    stacks = []
    moves = []
    with open(input_path, "r") as file:
        for line in file.read().splitlines():
            if "[" in line:
                stacks.append([line[i + 1:i + 2].strip() for i in range(0, len(line), 4)])
            elif "move" in line:
                parts = line.split(" ")
                moves.append([int(part) for part in [parts[1], parts[3], parts[5]]])
    rotated_stacks = list(zip(*stacks[::-1]))
    compact_stacks = [[crate for crate in stack if crate] for stack in rotated_stacks]
    return (compact_stacks, moves)

def move_crates(count, start, finish, stacks, reverse = True):
    group = stacks[start][count * -1:]
    if reverse:
        group = reversed(group)
    stacks[start] = stacks[start][0:count * -1]
    stacks[finish] = [*stacks[finish], *group]
    return stacks

def crate_mover(version, input_path):
    stacks, moves = parse_file(input_path)
    for move in moves:
        count, start, end = move
        stacks = move_crates(count, start - 1, end - 1, stacks, version == 9000)
    return "".join([str(stack[-1:][0]) for stack in stacks])

def ex1(input_path):
    return crate_mover(9000, input_path)

def ex2(input_path):
    return crate_mover(9001, input_path)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
