def find_marker(input, size):
    for i in range(0, len(input)):
        if len(list(set(input[i:i + size]))) == size:
            return i + size

def ex1(input_path):
    with open(input_path, "r") as file:
        data = file.read()
        return find_marker(data, 4)

def ex2(input_path):
    with open(input_path, "r") as file:
        data = file.read()
        return find_marker(data, 14)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
