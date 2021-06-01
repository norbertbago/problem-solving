# This is simple solution for easy sudoku 2 matrix
# Creat by Norbert Bago at 02/November/2020

sudoku2 = [0,4,3,2]
    
sudoku_numbers = list(range(1,5))

#Check if there is only one empty item
def last_empty_item(x):
    if x.count(0) == 1:
        return True
    else:
        return False

#fill one empty item 
def fill_last_item(x):
    for number in sudoku_numbers:
        if x.count(number) != 1:
            find_index = x.index(0)
            x[find_index] = number
            
        
#print sudoku2
def sudoku_matrix_print(x):
    print(x[0], end="  ")
    print(x[1], end="  ")
    print()
    print(x[2], end="  ")
    return x[3]

#sudoku2 solution
def sudoku2_solution(x):
    if last_empty_item:
        fill_last_item(x)
    
    return sudoku_matrix_print(x)

print("Sudoku without solution")
print(sudoku_matrix_print(sudoku2))
print()
print("Sudoku with solutions")
print(sudoku2_solution(sudoku2))
