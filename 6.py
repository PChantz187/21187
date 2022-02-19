import random 

board = [['  ' for i in range(8)] for i in range(8)]
alph = ["A", "B", "C", "D", "E", "F", "G", "H"]
white_player_points = 0
black_player_points = 0 


for times in range(0, 100):
    board = [['  ' for i in range(8)] for i in range(8)]
    black_queen_num = random.randrange(0, 8)
    black_queen_lett = random.choice(alph)
    index_bq = alph.index(black_queen_lett)
    board[black_queen_num][index_bq] = "Black Queen"

    white_tower_num = random.randrange(0, 8)
    white_tower_lett = random.choice(alph)
    index_wt = alph.index(white_tower_lett)
    while board[white_tower_num][index_wt] != '  ':
        white_tower_num = random.randrange(0, 8)
        white_tower_lett = random.choice(alph)
        index_wt = alph.index(white_tower_lett)
    board[white_tower_num][index_wt] = "White Tower"

    white_bishop_num = random.randrange(0, 8)
    white_bishop_lett = random.choice(alph)
    index_wb = alph.index(white_bishop_lett)
    while board[white_bishop_num][index_wb] != '  ':
        white_bishop_num = random.randrange(0, 8)
        white_bishop_lett = random.choice(alph)
        index_wb = alph.index(white_bishop_lett)
    board[white_bishop_num][index_wb] = "White Bishop"

    bl1 = False
    bl2 = False
    for i in range(8):
        if board[black_queen_num][i] == "White Bishop":
            bl1 = True 
        if board[black_queen_num][i] == "White Tower":
            bl2 = True 
    for j in range(8):
        if board[j][index_bq] == "White Bishop":
            bl1 = True 
        if board[j][index_bq] == "White Tower":
            bl2 = True
        if (white_bishop_num - black_queen_num == index_wb - index_bq) :
            bl1 = True
        elif (-white_bishop_num + black_queen_num == index_wb - index_bq):
            bl1 = True
        if (white_tower_num - black_queen_num == index_wt - index_bq) :
            bl2 = True
        elif (-white_tower_num + black_queen_num == index_wt - index_bq):
            bl2 = True
    


    if bl1 and bl2:
        black_player_points = black_player_points + 2
    elif bl1 and not bl2:
        black_player_points = black_player_points + 1
    elif not bl1 and bl2:
        black_player_points = black_player_points + 1

    
    whb_point = False
    wht_point = False
    for i in range(0, 8):
        if board[white_tower_num][i] == "Black Queen":
            wht_point = True
        if board[i][index_wt] == "Black Queen":
            wht_point = True
    
    def bishop_win(white_bishop_num, index_wb, black_queen_num, index_bq) :


        if (black_queen_num - white_bishop_num == index_bq - index_wb) :
            return True
        elif (-black_queen_num + white_bishop_num == index_bq - index_wb):
            return True
        else:
            return False

    
    if (bishop_win(white_bishop_num, index_wb, black_queen_num, index_bq)) :
        whb_point = True
    else :
        whb_point = False
    
    
    if whb_point and wht_point:
        white_player_points = white_player_points + 2 
    elif whb_point and not wht_point:
        white_player_points = white_player_points + 1
    elif not whb_point and wht_point:
        white_player_points = white_player_points + 1

print(white_player_points, black_player_points)