from collections import OrderedDict

#setting up letter to number translator
alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphstr = list(alph)
numbers = []
num = 1
while num < 53:
    numbers.append(num)
    num += 1

#setting up loop
setOfThree = []
i = 0
lineCounter = 0
value=0
#loop
while i < 100:
    #add three lines to "setofthree"
    with open("input.txt", "r") as g:
        for line in g.readlines()[lineCounter:lineCounter+3]:
            #adds three lines to "setofthree" as a string after removing duplicates and "/n" 
            setOfThree.append("".join(OrderedDict.fromkeys(line.strip())))

    #storing the lines in variables
    firstLine = str(setOfThree[0])
    secondline = str(setOfThree[1])
    thirdline = str(setOfThree[2])
    
    #matching first two, then seeing what matches in third
    snap = [i for i in firstLine if i in secondline]
    badge = [i for i in thirdline if i in snap]

    #turning array into string
    badgeLetter = badge[0]

    #letter to add points
    position = alphstr.index(badgeLetter)
    valueToAdd = numbers[position]
    value += valueToAdd

    #empty "setofthree" for next loops usage
    setOfThree.clear()

    #makes loops works n makes the right lines get chosen
    i += 1
    lineCounter += 3

#WOO FINAL VALUE
print(value)