def parse_instructions(input_path):
    with open(input_path, "r") as file:
        data = [[[int(value) for value in pos.split(",")] + ["#"] for pos in line.split(" -> ")] for line in file.read().splitlines()]
        for line in data:
            for i in range(len(line)):
                a = line[i]
                b = line[i + 1]
                if a[0] == b[0]:
                    # vertical
                    start, end = sorted([a[1], b[1]])
                    for j in range(start + 1, end):
                        line.append([a[0], j, "#"])
                else:
                    # horizontal
                    start, end = sorted([a[0], b[0]])
                    for j in range(start + 1, end):
                        line.append([j, a[1], "#"])
        points = []
        [[points.append(pos) for pos in line] for line in data]
        return (data, points)

def build_grid(points):
    points.append([500, 0, "+"])
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    min_x, max_x = [min(x), max(x)]
    min_y, max_y = [min(y), max(y)]
    grid = []
    for py in range(min_y-min_y, max_y-min_y + 1):
        grid.append([])
        for _ in range(min_x-min_x, max_x-min_x + 1):
            grid[py].append('.')
    for point in points:
        grid[point[1]-min_y][point[0]-min_x] = point[2]
    return grid

class Grain:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def try_move(self, grid):
        y = self.y + 1
        for x in [self.x, self.x - 1, self.x + 1]:
            if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
                return None # lost
            else:
                if grid[y][x] == ".":
                    self.x = x
                    self.y = y
                    return True
        return False

def simulate_sand(grid, draw):
    did_move = False
    grain = Grain(grid[0].index("+"), 0)
    while(True):
        did_move = grain.try_move(grid)
        if draw:
            print("")
            for y, line in enumerate(grid):
                if grain.y == y:
                    new_line = [*line]
                    new_line[grain.x] = "x"
                    print("".join(new_line))
                else:
                    print("".join(line))
        if did_move != True:
            break
    lost = did_move == None
    return (grain, lost)

def ex1(input_path, draw = False):
    _, points = parse_instructions(input_path)
    grid = build_grid(points)
    sand = 0

    while(True):
        grain, lost = simulate_sand(grid, draw)
        if (lost):
            break
        grid[grain.y][grain.x] = "o"
        sand += 1
    return sand

def ex2(input_path):
    return 2

if __name__ == "__main__":
    input_path = "./input.txt"
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
