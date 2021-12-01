
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
increases = 0

for i in range(1, len(data)):
    print(f"data was {data[i - 1]} and data index {i} is {data[i]}")

    prev_depth = int(data[i -1].strip())
    depth = int(data[i].strip())

    if prev_depth < depth:
        increases = increases + 1
        print(f"  There was an increase, now at {increases}")

print(f"total increases: {increases}")

