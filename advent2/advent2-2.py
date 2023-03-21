score = 0
outcomeList = []
outcomeDict = {"A X" : 3,"B X": 1, "C X": 2, "A Y": 4, "B Y": 5, "C Y": 6, "A Z": 8, "B Z": 9, "C Z": 7 }

with open("input.txt", "r") as f:
    for line in f.readlines():
        outcomeList.append(line)

for i in outcomeList:
    score += outcomeDict[i.strip()]

print(score)