
def read_input():
    lines = None
    # with open('input.txt') as f:
    with open('test.txt') as f:
        lines = f.readlines()

    if lines == None:
        exit
    else:
        return lines   


closing_chars = [')', '}', '>', ']']
# global indent

def get_indent(indent: int):
    indent_str = ""
    for x in range(indent):
        indent_str = indent_str + "  "
    return indent_str


# TODO: figure out issue with end of the line indexing

def check_chunk(line, starting_index, indent):
    chunk_start = line[starting_index]
    chunk_end_char = get_expected_end(chunk_start)
    print(f"{get_indent(indent)}chunk start: '{chunk_start}', starting_index: {starting_index}, looking for end '{chunk_end_char}'")
    found_end = False
    # next_index = starting_index;

    c_idx = starting_index + 1
    next_index = c_idx;
    while c_idx != -1:
        if c_idx == len(line) - 1:
            # end of the line
            next_index = - 1
        else:
            
            # next_index = next_index + 1
            next_index = c_idx + 1 
            print(f"{get_indent(indent)}next_index incremented to: {next_index}")

        print(f"{get_indent(indent)}checking next char '{line[c_idx]}' at index {c_idx}, next_index: {next_index}")
        if line[c_idx] in closing_chars:
            if line[c_idx] == chunk_end_char:
                found_end = True
                # next_index = next_index + 1
                print(f"{get_indent(indent)}found end! next_index incremented to: {next_index}")
                # TODO: how to check the next chunk in the line? return with a start index?
                break
            elif line[c_idx] in closing_chars:
                #incorrect close
                print(f"{get_indent(indent)}Closed chunk starting with '{chunk_start}' with wrong closer line[c_idx]")
                # next_index = -1
                break
        else:
            # step down into next chunk
            indent = indent + 1
            # print(f"{get_indent(indent)}substring: {line[1:len(line) - 1]}")

            print(f"{get_indent(indent)}recuring with string: {line}, start_index: {c_idx} ")
            # c_idx = check_chunk(line[1:len(line) - 1], c_idx, indent) - 1 # do the -1 since we increment after the loop
            c_idx = check_chunk(line, c_idx, indent) - 1 # do the -1 since we increment after the loop
            indent = indent - 1
        
        c_idx = c_idx + 1

        # debug
        # break


    if found_end == False:
        print(f"{get_indent(indent)}Didn't close chunk starting with '{chunk_start}' at index {c_idx} ")
    else:
        print(f"{get_indent(indent)}Close chunk starting with '{chunk_start}' at index {c_idx}, returning next_index: {next_index} ")

    return next_index


def get_expected_end(character):
    expected_end = ''
    if character == '(':
        expected_end = ')'
    elif character == '{':
        expected_end = '}'
    elif character == '<':
        expected_end = '>'
    elif character == '[':
        expected_end = ']'
    else:
        print(f"Unexpected character")

    return expected_end



indent = 0


data = read_input()


for line in data:
    print(f"line: {line.strip()}")
    next_index = 0

    # while next_index > -1:
    next_index = check_chunk(line.strip(), next_index, indent)
    # debug
    break
    #    next_index = -1
    



