#2d lists & nested loops

#2d lists       #creating grid like structure in python using 2d lists
number_grid = [
    #c1 #c2 #c3     #columns
    [1 , 2 , 3],  #row 0
    [4 , 5 , 6],  #row 1
    [7 , 8 , 9],  #row 2
    [0]           #row 3
]
#accessing individual elements inside the list -> print(name of list[row][column])
print(number_grid[0][0])
print(number_grid[2][1])

#nested for loop - for loop inside a for loop
for row in number_grid:
    print(row)
print('')
for row in number_grid:
    for col in row:
        print(col)