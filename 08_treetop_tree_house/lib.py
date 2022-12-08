from os import read
from math import prod

def map_trees(data, x, y):
    tree_map = {
        "top": [],
        "left": [],
        "bottom": [],
        "right": []
    }
    for i in range(y):
        tree_map["top"].insert(0, int(data[i][x]))
    for i in range(x):
        tree_map["left"].insert(0, int(data[y][i]))
    for i in range(y + 1, len(data)):
        tree_map["bottom"].append(int(data[i][x]))
    for i in range(x + 1, len(data[y])):
        tree_map["right"].append(int(data[y][i]))
    return tree_map

def is_visible(tree_map, value):
    for dir in tree_map.keys():
        if all(x < value for x in tree_map[dir]):
            return True

def ex1(input_path):
    with open(input_path, "r") as file:
        data = file.read().splitlines()
        visible = 0
        for y in range(len(data)):
            for x in range(len(data[y])):
                tree_map = map_trees(data, x, y)
                value = int(data[y][x])
                if x == 0 or y == 0 or x == len(data[y])-1 or y == len(data)-1 or is_visible(tree_map, value):
                    visible += 1
        return visible

def get_scenic_score(tree_map, value):
    scenic_score = []
    for trees in tree_map.values():
        score = 0
        for tree in trees:
            score += 1
            if tree >= value:
                break
        scenic_score.append(score)
    return prod(scenic_score)

def ex2(input_path):
    with open(input_path, "r") as file:
        data = file.read().splitlines()
        scenic_scores = []
        for y in range(len(data)):
            for x in range(len(data[y])):
                tree_map = map_trees(data, x, y)
                value = int(data[y][x])
                scenic_scores.append(get_scenic_score(tree_map, value))
        return max(scenic_scores)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
