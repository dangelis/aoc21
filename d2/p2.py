
def read_input():
    lines = None
    with open('input.txt') as f:
    # with open('test.txt') as f:
        lines = f.readlines()

    if lines == None:
        exit
    else:
        return lines   

data = read_input()

depth = 0
distance = 0
aim = 0

for i in data:
    inst = i.split(" ")

    if inst[0] == "forward":
        distance = distance + int(inst[1])
        depth = depth + aim * int(inst[1])
    elif inst[0] == "up":
        aim = aim - int(inst[1])
    else: #down
        aim = aim + int(inst[1])

    print(f"dist: {distance}, depth: {depth}")

print(f"depth distance product: {depth * distance}")




