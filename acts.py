
for s in range(5,1,-1):
    print("*" * s )
    if s == 2: 
        print("", end = "*   ") 
for s in range(1,6,1):
    print("*" * s )

palin = input("Enter a word: ").lower().split()

for pal in range(len(palin)):
    if palin[0] == palin[-1]:
        print("Palindrome")
        break
    else:
        print("not palindrome")




rows = int(input("rows: "))
columns = int(input("columns: "))

for i in range(rows):
    
    for j in range(columns):
        
        if(i == 0 or i == rows - 1 or j == 0 or j == columns - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()

"""
row = 1
column = 1
while row <= rows:
    if (row == 2 or row ==  rows):
        print('*' *5 , end = '  ')
    else:
        print(' ', end = '  ')
    row +=1
while column <= columns:
    if (column == 2 or column ==  columns):
        print('*' *5 , end = '  ')
    else:
        print(' ', end = '  ')
    column +=1"""