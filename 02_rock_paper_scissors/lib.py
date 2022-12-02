shape_map = { 'X': 'A', 'Y': 'B', 'Z': 'C' }
points_map = { 'A': 1, 'B': 2, 'C': 3 }
move_map = {
    'A': ['C', 'A', 'B'],
    'B': ['A', 'B', 'C'],
    'C': ['B', 'C', 'A']
}
outcome_map = { 'X': 0, 'Y': 1, 'Z': 2 }

def play_tournament(input_path, func):
    with open(input_path, "r") as file:
        rounds = file.read().strip().split("\n")
        return sum(map(lambda round: play_round(round, func), rounds))

def play_round(round, func):
    opponent, player = map(points_map.get, func(*round.strip().split(" ")))
    return calculate_score(opponent, player)

def choose_shape(opponent, player):
    return opponent, shape_map[player]

def choose_outcome(opponent, player):
    return opponent, move_map[opponent][outcome_map[player]]

def calculate_score(opponent, player):
    if abs(opponent - player) == 2: # rock beats scissors
        return player + (6 if player == 1 else 0)
    elif opponent < player: # scissors beats paper, paper beats rock
        return player + 6
    elif opponent == player: # draw
        return player + 3
    else: # lose
        return player

def ex1(input_path):
    return play_tournament(input_path, choose_shape)

def ex2(input_path):
    return play_tournament(input_path, choose_outcome)

if __name__ == "__main__":
    input_path = './input.txt'
    print("Exercise 1:", ex1(input_path))
    print("Exercise 2:", ex2(input_path))
