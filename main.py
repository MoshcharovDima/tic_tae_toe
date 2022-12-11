def print_game(matrix):
    print('  1 2 3')
    i = 1
    for array in matrix:
        print(i, end=' ')
        i += 1
        for ellements in array:
            if ellements == 0:
                print('-', end=' ')
            if ellements == 1:
                print('*', end=' ')
            if ellements == 2:
                print('o', end=' ')
        print()
def end_game(matrix):
    flag = 0
    counterer_1 = 0
    counterer_2 = 0
    counterer_1_1 = 0
    counterer_1_2 = 0
    for i in range(3):
        if matrix[i].count(1) == 3:
            print("1 player win")
            flag = 1
        if matrix[i].count(2) == 3:
            print("2 player win")
            flag = 1
    trans_matrix = [[matrix[j][i] for j in range(3)] for i in range(3)]
    for i in range(3):
        if trans_matrix[i].count(1) == 3:
            print("1 player win")
            flag = 1
        if trans_matrix[i].count(2) == 3:
            print("2 player win")
            flag = 1
    for i in range(3):
        if matrix[i][2-i] == 1:
            counterer_1 +=1
        if matrix[i][2-i] == 2:
            counterer_2 +=1
        if matrix[2-i][2] == 1:
            counterer_1_1 +=1
        if matrix[2-i][2] == 2:
            counterer_1_2 +=1
    if counterer_1 == 3 or counterer_1_1 == 3:
        print("1 player win")
        flag = 1
    if counterer_2 == 3 or counterer_1_2 == 3:
        print("2 player win")
        flag = 1
    return flag
field = [[0 for i in range(3)] for j in range(3)]
counter = 1
print("""Players take turns
You need to enter 2 numbers from 1 to 3
1 number is responsible for the string
2 number is responsible for column""")
while end_game(field) != 1:
    print_game(field)
    if counter == 10:
        print("Friendship win")
        break
    print(f"Player {2 - counter % 2}")
    try:
        a, b = (input("Enter 2 numbers from 1 to 3\n").split())
        a = int(a)
        b = int(b)
    except ValueError:
        print("Invalid Input!!! Try Again")
        continue
    if a > 3 or a < 1 or b < 1 or b > 3:
        print("Invalid Input!!! Try Again")
        continue
    if field[a - 1][b - 1] != 0:
        print("Oops! The Place is already occupied. Try again!!")
        continue
    field[a - 1][b - 1] = 2 - counter % 2
    counter += 1
print_game(field)