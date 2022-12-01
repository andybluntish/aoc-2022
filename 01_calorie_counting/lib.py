def calories_per_elf(input_path):
    with open(input_path, 'r') as file:
        data = file.read()
        elves = data.strip().split("\n\n")
        results = []

        for elf in elves:
            fruit = map(int, elf.split("\n"))
            results.append(sum(fruit))

        return results

def calories_per_elf_golf(input_path):
    with open(input_path, 'r') as file:
        return map(lambda elf: sum(map(int, elf.split("\n"))), file.read().strip().split("\n\n"))

def ex1(input_path):
    return max(calories_per_elf(input_path))

def ex2(input_path):
    return sum(sorted(calories_per_elf(input_path), reverse=True)[0:3])

if __name__ == '__main__':
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
