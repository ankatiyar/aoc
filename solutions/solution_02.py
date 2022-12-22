with open('../inputs/input02.txt') as f:
    lines = f.readlines()

moves = dict({"A X": 4, "A Y": 8, "A Z": 3, "B X": 1, "B Y": 5, "B Z": 9, "C X": 7, "C Y": 2, "C Z": 6})
outcome = dict({"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7})
total1 = 0
total2 = 0
for line in lines:
    total1 = total1 + moves[line[:-1]]
    total2 = total2 + outcome[line[:-1]]
print("Score 1: ", total1)
print("Score 2: ", total2)
