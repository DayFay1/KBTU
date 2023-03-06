import random

N = 50
M = 6

def play_game():
    faces = [random.randint(1, M) for i in range(N)]
    points = 0
    for i in range(1, M+1):
        count = faces.count(i)
        if count > 1:
            points += count * i
            points -= count * count
    return points

num_trials = 100000
total_points = sum([play_game() for i in range(num_trials)])
expected_points = total_points / num_trials

print(round(expected_points, 2))