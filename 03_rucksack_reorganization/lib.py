import string

def score_duplicates(pack):
    mid = len(pack)//2
    a, b = [pack[:mid], pack[mid:]]
    for char in a:
        if char in b:
            return get_score(char)

def score_common_in_group(group):
    first, rest = [group[0], group[1:]]
    for char in first:
        if char in rest[0] and char in rest[1]:
            return get_score(char)

def get_score(char):
    base = 27 if char.isupper() else 1
    return base + string.ascii_lowercase.index(char.lower())

def ex1(input_path):
    with open(input_path, "r") as file:
        packs = file.read().strip().split("\n")
        return sum([score_duplicates(pack) for pack in packs])

def ex2(input_path):
    groups = []
    with open(input_path, "r") as file:
        packs = file.read().strip().split("\n")
        for i in range(0, len(packs), 3):
            group = packs[i:i + 3]
            groups.append(score_common_in_group(group))
    return sum(groups)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
