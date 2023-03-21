score = 0
outcomeList = []
outcomeDict = {"A X" : 0,"B X": 0, "C X": 0, "A Y": 3, "B Y": 3, "C Y": 3, "A Z": 6, "B Z": 6, "C Z": 6 }

with open("input.txt", "r") as f:
    for line in f.readlines():
        outcomeList.append(line)
        if "X" in line:
            score += 1
        elif "Y" in line:
            score += 2
        elif "Z" in line:
            score += 3

for i in outcomeList:
    score += outcomeDict[i.strip()]

print(score)

        
    


    
