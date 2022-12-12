def get_cycles(input_path):
    cycles = [1]
    with open(input_path, "r") as file:
        for instruction in file.read().splitlines():
            cycles.append(cycles[-1])
            parts = instruction.split(" ")
            if len(parts) == 2:
                cycles.append(cycles[-1] + int(parts[1]))
    return cycles

def ex1(input_path):
    cycles = get_cycles(input_path)
    results = []
    for i in range(len(cycles)):
        if i % 40 == 20:
            results.append(cycles[i-1] * i)
    return sum(results)

def ex2(input_path):
    cycles = get_cycles(input_path)
    width = 40
    screen = []
    for y in range(6):
        screen.append("")
        for x in range(width):
            index = x + (width * y)
            value = "#" if x in range(cycles[index] - 1, cycles[index] + 2) else "."
            screen[y] += value
    return "\n".join(screen)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:")
    print(ex2(input_path))
