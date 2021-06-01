# This is simple solution for easy,normal and difficult binary sudoku
# Creat by Norbert Bago at 03/January/2021

easy_binary_sudoku = [1, 0, 9, 1]
normal_binary_sudoku = [9, 0, 9, 1]
difficult_binary_sudoku = [9, 9, 1, 9]


#Check if there is only one empty item
def last_empty_item(x):
    if x.count(9) == 1:
        return True
    else:
        return False

#fill one empty item 
def fill_last_item(x):
    find_index = x.index(9)
    if x[0] == 1:
        x[find_index] = 0
    else:
        x[find_index] = 1

def fill_two_item(x):
    if x[0] == 1:
        x[-1] = 1
    elif x[0] == 0:
        x[-1] = 0
    elif x[0] == 9 and x[1] == 1 or x[2] == 1:
        x[0] = 0
    elif x[0] == 9 and x[1] == 0 or x[2] == 0:
        x[0] = 1
    
def fill_three_item(x):
    if x[0] == 1 or x[-1] == 0:
        x[1] = 0

    elif x[1] == 1 or x[2] == 1:
        x[-1] = 0

#print binary sudoku2
def sudoku_matrix_print(x):
    print(x[0], end="  ")
    print(x[1], end="  ")
    print()
    print(x[2], end="  ")
    return x[3]

#binary sudoku 2x2 solution
def binary_sudoku2_solution(x):
    empty_count = x.count(9)
    while empty_count != 0:
        if empty_count == 1:
            fill_last_item(x)
        elif empty_count == 2:
            fill_two_item(x)
        elif empty_count == 3:
            fill_three_item(x)
        empty_count = x.count(9)

       
    return sudoku_matrix_print(x)


print("Easy Binary Sudoku with solutions")
print(binary_sudoku2_solution(easy_binary_sudoku))
print()
print("Normal Binary Sudoku with solutions")
print(binary_sudoku2_solution(normal_binary_sudoku))
print()
print("Difficult Binary Sudoku with solutions")
print(binary_sudoku2_solution(difficult_binary_sudoku))
print()
