import copy

def read_input():
    lines = None
    with open('input.txt') as f:
    # with open('test.txt') as f:

    # with open('col_test.txt') as f:
        lines = f.readlines()

    if lines == None:
        exit
    else:
        return lines   

# Turn a line in input into ints and clean up empty values due to my lazy parsing
def transform_line(board_line_list: list):
    new_int_list = []

    for value in range(len(board_line_list)):
        # Because I'm too lazy to make a better parser
        if board_line_list[value] != "":
            new_int_list.append(int(board_line_list[value]))
    
    return new_int_list


def check_number(num: int, board: list, board_index: int, board_found_list: list):
    # print(f"checking for number {num} on board {board_index}")
    # Check rows
    found_idx = -1
    row_idx = 0
    for row in board:
        try:
            found_idx = row.index(num)

            # What if there are multiple machtes per row -- doesn't look like they exist
            # found_indexes = [i for i, x in enumerate(row) if x == num]
            # if len(found_indexes) > 1:
            #     print(f"Found a multiliner!!!!!!")

            # print(f"    found match at board {board_idx}, row {row_idx}, column {found_idx}")
            board_found_list[board_index][row_idx][found_idx] = True
            # for board in board_found_list:
            #     # print(f"        {board}")
        except ValueError:
            pass
        row_idx = row_idx + 1

    # Return the winning board index (-1 if none found)
    return check_bingo(board_found_list[board_index], board_idx)


def check_bingo_row(boolean_board: list, board_idx: int):
    winning_board_idx = -1

    # print(f"  checking rows")
    
    for row in boolean_board:
        row_check = True
        # print(f"    checking row: {row}")
        for val in row:
            row_check = row_check and val


        if row_check == True:
            print(f"    row_check is true for row {row}")
            winning_board_idx = board_idx
            break

    return winning_board_idx



def check_bingo_col(boolean_board: list, board_idx: int):
    for col_idx in range(len(boolean_board)):
        winning_board_idx = -1
        col_check = True
        # print(f"    checking column {col_idx}")
        for row_idx in range(len(boolean_board)):
            
            col_check = boolean_board[row_idx][col_idx] and col_check
            # print(f"    at ({col_idx}, {row_idx}) value is {board[row_idx][col_idx]}:")
        if col_check == True:
            print(f"    col_check is true")
            winning_board_idx = board_idx
            break
        
    return winning_board_idx



# def check_bingo(board_found_list: list):
def check_bingo(boolean_board: list, board_idx: int):

    winning_board_idx = -1
    winning_board_idx = check_bingo_row(boolean_board, board_idx)
    if winning_board_idx > -1:
        return winning_board_idx
    
    # Check columns
    winning_board_idx = check_bingo_col(boolean_board, board_idx)   
    return winning_board_idx


def print_board(board_idx):
    # Print winning board showing marked numbers
    print(f"board: {board_idx}")
    for row_idx in range(len(boards_found_number_list[board_idx])):
        col_idx = 0
        for row_val in boards_found_number_list[board_idx][row_idx]:
            if row_val == False:
                print(f"     {boards[board_idx][row_idx][col_idx]}", end = '')
            else:
                print(f"    [{boards[board_idx][row_idx][col_idx]}]", end = '')
            col_idx = col_idx + 1
        print(f"")

def print_boards(boards):
    for board_idx in range(len(boards)):
        print_board(board_idx)

#################################

data = read_input()

drawn_numbers_strings = data[0].strip().split(",")
drawn_numbers = []
for i in drawn_numbers_strings:
    drawn_numbers.append(int(i))
    
del(data[0]) # Remove the top lines so that what's left is just the board data
del(data[0])

print(f"drawn_numbers: {drawn_numbers}")

# Build the boards
boards_found_number_list = [None]
board_found_number_list = []

boards = [None]
board = []
board_idx = 0;

for line in data:
    if line != "\n":
        board_line_list = line.strip().split(" ")
        board_line_int_list = transform_line(board_line_list)
        board.append(board_line_int_list)

        default_found_row = [False] * len(board[0])
        board_found_number_list.append(default_found_row)
    elif len(board) > 0:
        boards[board_idx] = copy.deepcopy(board)
        boards_found_number_list[board_idx] = copy.deepcopy(board_found_number_list)

        board.clear()
        board_found_number_list.clear()

        boards.append([None])
        boards_found_number_list.append([None])

        board_idx = board_idx + 1

# Grab the last one
boards[board_idx] = copy.deepcopy(board)
boards_found_number_list[board_idx] = copy.deepcopy(board_found_number_list)

# print(f"boards:")
# for board in boards:
#     print(f"board:\n{board}")

# print(f"boards_found_number_list:")
# for board in boards_found_number_list:
#     print(f"board:\n{board}")



# Play bingo
last_num = -1
won_boards = []

for num in drawn_numbers:
    print(f"Try number {num}")
    last_num = num
    winning_board_idx = -1

    for board_idx in range(len(boards)):
        if board_idx in won_boards:
            print(f"    skipping board {board_idx} since it already won")
            continue
        winning_board_idx = check_number(num, boards[board_idx], board_idx, boards_found_number_list)
        if winning_board_idx > -1:
            print(f"winning board found at board {board_idx}!")
            # print("Boards now:")
            # print_boards(boards)
            won_boards.append(board_idx)

    if len(boards) == len(won_boards):
        break



last_winning_board = won_boards[len(won_boards) - 1]
print(f"last winning board found at board {last_winning_board}!")

# print(f"boards_found_number_list\n")
# for found in boards_found_number_list:
#     print(f"{found}")

# Calculate the score
print(f"Calculating score:")
winning_board_sum = 0
for row_idx in range(len(boards_found_number_list[last_winning_board])):
    col_idx = 0
    for row_val in boards_found_number_list[last_winning_board][row_idx]:
        if row_val == False:
            winning_board_sum = winning_board_sum + boards[last_winning_board][row_idx][col_idx]
            print(f"Adding {boards[last_winning_board][row_idx][col_idx]}, sum now {winning_board_sum}")
        col_idx = col_idx + 1


# Print the boards showing marked numbers
# print(f"boards state:")
# print_boards(boards)

# Print winning board showing marked numbers
print_board(last_winning_board)

print(f"Number of boards: {len(boards)}")
print(f"winning_board_sum = {winning_board_sum}, last_num: {last_num}, product: {winning_board_sum * last_num}")

# ! 0 
# 11200 too high
# 2568



        