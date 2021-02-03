
# create the board
cb={'8a':'wrook','8b':'wknight','8c':'wbishop','8d':'wking','8e':'wqueen','8f':'wbishop','8g':'wknight','8h':'wrook',
'7a':'wpawn','7b':'wpawn','7c':'wpawn','7d':'wpawn','7e':'wpawn','7f':'wpawn','7g':'wpawn','7h':'wpawn',
'6a':' ','6b':' ','6c':' ','6d':' ','6e':' ','6f':' ','6g':' ','6h':' ',
'5a':' ','5b':' ','5c':' ','5d':' ','5e':' ','5f':' ','5g':' ','5h':' ',
'4a':' ','4b':' ','4c':' ','4d':' ','4e':' ','4f':' ','4g':' ','4h':' ',
'3a':' ','3b':' ','3c':' ','3d':' ','3e':' ','3f':' ','3g':' ','3h':' ',
'2a':'bpawn','2b':'bpawn','2c':'bpawn','2d':'bpawn','2e':'bpawn','2f':'bpawn','2g':'bpawn','2h':'bpawn',
'1a':'brook','1b':'bknight','1c':'bbishop','1d':'bking','1e':'bqueen','1f':'bbishop','1g':'bknight','1h':'brook'}

def isValidChessboard(board):
    boardisready = 0
    # Only 16 black pieces and only 8 pawns

    # Loop and Get key

    bpiece = 0
    wpiece = 0
    for val in board.values():
        # if key starts with 'b', bkey += 1
        if val[0] == 'b':
            bpiece += 1
        # if key starts with 'w', wkey += 1
        elif val[0] =='w':
            wpiece += 1
        elif val == ' ':
            None
    # if bkey > 16 or wkey > 16
    if bpiece > 16 or wpiece > 16:
        # Generate error
        boardisready += 0
    else:
        boardisready += 1
     
    bpawn = 0
    wpawn = 0
    for val in board.values():
        # if value is 'bpawn', bpawnvalue += 1
        if val == 'bpawn':
            bpawn += 1
        # if value is 'wpawn', wpawnvalue += 1
        elif val == 'wpawn':
            wpawn += 1
        # if bpawnvalue >= 8 or wpawnvalue >= 8
    if bpawn <= 8 and wpawn <= 8:
        boardisready += 1
    else:
        boardisready += 0
    
    # all pieces must be on a valid space from 1a to 8h
    ycord = ['a','b','c','d','e','f','g','h']
    xcord = ['1','2','3','4','5','6','7','8']
    carteez = []
    for y in ycord:
        for x in xcord:
            carteez.append(x+y)
            carteez.reverse
            carteez.sort()

    cblist = list(board.keys())
    cblist.sort()

    if carteez != cblist:
        boardisready += 0
    else:
        boardisready += 1
    
    if boardisready == 3:
        return True
    else:
        return False



def printBoard(board):
    print(board['8a'] + '|' + board['8b'] + '|' + board['8c'] + '|' + board['8d'] + '|' + board['8e'] + '|' + board['8f'] + '|' + board['8g'] + '|' + board['8h'])
    print(board['7a'] + '|' + board['7b'] + '|' + board['7c'] + '|' + board['7d'] + '|' + board['7e'] + '|' + board['7f'] + '|' + board['7g'] + '|' + board['7h'])
    print(board['6a'] + '|' + board['6b'] + '|' + board['6c'] + '|' + board['6d'] + '|' + board['6e'] + '|' + board['6f'] + '|' + board['6g'] + '|' + board['6h'])
    print(board['5a'] + '|' + board['5b'] + '|' + board['5c'] + '|' + board['5d'] + '|' + board['5e'] + '|' + board['5f'] + '|' + board['5g'] + '|' + board['5h'])
    print(board['4a'] + '|' + board['4b'] + '|' + board['4c'] + '|' + board['4d'] + '|' + board['4e'] + '|' + board['4f'] + '|' + board['4g'] + '|' + board['4h'])
    print(board['3a'] + '|' + board['3b'] + '|' + board['3c'] + '|' + board['3d'] + '|' + board['3e'] + '|' + board['3f'] + '|' + board['3g'] + '|' + board['3h'])
    print(board['2a'] + '|' + board['2b'] + '|' + board['2c'] + '|' + board['2d'] + '|' + board['2e'] + '|' + board['2f'] + '|' + board['2g'] + '|' + board['2h'])
    print(board['1a'] + '|' + board['1b'] + '|' + board['1c'] + '|' + board['1d'] + '|' + board['1e'] + '|' + board['1f'] + '|' + board['1g'] + '|' + board['1h'])

validBoard = isValidChessboard(cb)
if validBoard:
    printBoard(cb)
else:
    print("There is an error with the board")