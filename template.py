
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


