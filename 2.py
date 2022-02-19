import random

board = [['0' for i in range(3)] for i in range(3)]
print(board)
#Δημιουργία λίστας με καπάκια, 1 = μικρό 2 = μεσαίο 3 = μεγάλο
Cap_List = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]

Av_steps = 0
Ov_steps = 0
win = False

for index in range(100):
    board = [['0' for i in range(3)] for i in range(3)]
    Cap_List = [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3]
    win = False
    steps = 0 
    while not win:
        place = random.randrange(len(Cap_List))
        item = Cap_List[place]
        while item == 0:
            place = random.randrange(len(Cap_List))
            item = Cap_List[place]
            print(item)
        r_row = random.randrange(3)
        r_column = random.randrange(3)
        curr = board[r_row][r_column]
        int_item = int(item)
        int_curr = int(curr)
        while board[r_row][r_column] != 0 and int_item > int_curr:
            r_row = random.randrange(3)
            r_column = random.randrange(3)
        board[r_row][r_column] = item
        steps = steps + 1
        
        if board[0][r_column] == item and board[1][r_column] == item and board[2][r_column] == item:
            win = True
        elif board[0][r_column] == 1 and board[1][r_column] == 2 and board[2][r_column] == 3:
            win = True
        elif board[r_row][0] == item and board[r_row][1] == item and board[r_row][2] == item:
            win = True
        elif board[r_row][0] == 1 and board[r_row][1] == 2 and board[r_row][2] == 3:
            win = True
        elif board[0][0] == item and board[1][1] == item and board[2][2] == item:
            win = True
        elif board[0][2] == item and board[1][1] == item and board[2][0] == item:
            win = True
        elif board[0][0] == 1 and board[1][1] == 2 and board[2][2] == 3:
            win = True
        elif board[0][2] == 1 and board[1][1] == 2 and board[2][0] == 3:
            win = True
    Ov_steps = Ov_steps + steps

Av_steps = Ov_steps / 100
print("Overal Steps:")
print(Ov_steps)
print("Average Steps:")
print(Av_steps)






