alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphstr = list(alph)
numbers = []
num = 1
value = 0
while num < 53:
    numbers.append(num)
    num += 1
print(alphstr[51])

with open("input.txt", "r") as f:
    for line in f.readlines():
        lineLength = len(line)
        lineArray = list(line) #puts line in array

        firstHalf = line[:int(len(line)/2)]
        secondHalf = line[int(len(line)/2):]
        matches = [i for i in firstHalf if i in secondHalf]
        matched = matches.pop()
        print(matched)
        position = alphstr.index(matched)
        ballsnumbers = numbers[position]

        value += ballsnumbers
        
print(value)









        