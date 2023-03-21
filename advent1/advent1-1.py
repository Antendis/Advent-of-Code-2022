
name = []
sum_of_num = 0
with open("input.txt", "r") as f:
    for line in f.readlines():
        if line == "\n":
            name.append(sum_of_num)
            sum_of_num = 0
        if line != "\n":
            stored_num = line
            sum_of_num = int(stored_num) + int(sum_of_num)

    biggest = max(name)
    print(biggest)
