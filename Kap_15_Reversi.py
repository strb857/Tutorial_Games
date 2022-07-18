#Reversi
import random
import sys
WIDTH = 8 #Board dimentions
HEIGHT = 8
def drawBoard(board):
    #Return None - draws the boars as passed in "board"
    print('  12345678')
    print(' +--------+')
    for y in range(HEIGHT):
        print('%s|' % (y+1), end='')
        for x in range(WIDTH):
            print(board[x][y], end='')
        print('|%s' % (y+1))
    print(' +--------+')
    print('  12345678')

def getNewBoard():
    #Returns blank board - Create blank board data structure
    board = []
    for i in range(WIDTH):
        board.append(' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ')
    return board

#def isValidMove(board, title, xstart, ystart):