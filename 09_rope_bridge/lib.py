class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.history = [str(self)]

    def __str__(self):
        return f"{self.x}:{self.y}"

    def move(self, dir, dist = 1):
        if dir == "U":
            self.y -= dist
        elif dir == "D":
            self.y += dist
        elif dir == "L":
            self.x -= dist
        elif dir == "R":
            self.x += dist

    def record_history(self):
        self.history.append(str(self))

def move_knot(knot, target):
    if target.x in range(knot.x - 1, knot.x + 2) and target.y in range(knot.y - 1, knot.y + 2): # touching
        return
    elif target.x == knot.x:
        knot.move("D") if target.y > knot.y else knot.move("U")
    elif target.y == knot.y:
        knot.move("R") if target.x > knot.x else knot.move("L")
    else: # diagonal
        knot.move("R") if target.x > knot.x else knot.move("L")
        knot.move("D") if target.y > knot.y else knot.move("U")
    knot.record_history()

def move_knots(count, step_input):
    knots = [Point() for _ in range(count)]
    with open(step_input, "r") as file:
        for step in file.read().splitlines():
            dir, dist = step.split(" ")
            for _ in range(int(dist)):
                knots[0].move(dir)
                for i in range(len(knots)-1):
                    move_knot(knots[i + 1], knots[i])
    return len(set(knots[-1].history))

def ex1(input_path):
    return move_knots(2, input_path)

def ex2(input_path):
    return move_knots(10, input_path)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
