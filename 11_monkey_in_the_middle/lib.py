from math import prod

class Monkey:
    def __init__(self, id, items, op, fac, div, targets):
        self.id = id
        self.items = items
        self.op = op
        self.fac = fac
        self.div = div
        self.targets = targets
        self.count = 0

    def __lt__(self, other):
         return self.count < other.count

    def inspect(self, item, value):
        if self.op == "+":
            result = item + value
        else:
            result = item * value
        return result

    def turn(self, relief=True, mod=None):
        while len(self.items):
            item = self.items.pop(0)
            fac = item if self.fac == "old" else self.fac
            item = item * fac if self.op == "*" else item + fac
            if relief:
                item = item // 3
            else:
                item = item % mod
            target = self.targets[0 if item % self.div == 0 else 1]
            target.items.append(item)
            self.count += 1

def parse_input(input_path):
    monkies = []
    with open(input_path, "r") as file:
        for monkey in [line.strip() for line in file.read().split("\n\n")]:
            data = [line.strip() for line in monkey.splitlines()]
            id = int(data[0][-2:-1])
            items = [int(item) for item in data[1].split(": ")[1].split(", ")]
            op, fac = data[2].split(" ")[-2:]
            fac = int(fac) if fac.isdigit() else fac
            div = int(data[3].split(" ")[-1])
            targets = [int(line.split(" ")[-1]) for line in data[-2:]]
            monkies.append(Monkey(id, items, op, fac, div, targets))
    for monkey in monkies:
        monkey.targets = list(map(lambda id: monkies[id], monkey.targets))
    return monkies

def ex1(input_path):
    monkies = parse_input(input_path)
    for _ in range(20):
        for monkey in monkies:
            monkey.turn()
    return prod(sorted([m.count for m in monkies])[-2:])

def ex2(input_path):
    monkies = parse_input(input_path)
    mod = prod([m.div for m in monkies])
    for _ in range(10000):
        for monkey in monkies:
            monkey.turn(relief=False, mod=mod)
    return prod(sorted([m.count for m in monkies])[-2:])

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
