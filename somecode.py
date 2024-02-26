import random, sys
try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    sys.exit()

BOARD_WIDTH = 16  # (!) Try changing this to 4 or 40.
BOARD_HEIGHT = 14  # (!) Try changing this to 4 or 20.
MOVES_PER_GAME = 20  # (!) Try changing this to 3 or 300.

HEART     = chr(9829)  # Character 9829 is '♥'.
DIAMOND   = chr(9830)  # Character 9830 is '♦'.
SPADE     = chr(9824)  # Character 9824 is '♠'.
CLUB      = chr(9827)  # Character 9827 is '♣'.
BALL      = chr(9679)  # Character 9679 is '•'.
TRIANGLE  = chr(9650)  # Character 9650 is '▲'.

BLOCK     = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN    = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT  = chr(9488)  # Character 9488 is '┐'
UPRIGHT   = chr(9492)  # Character 9492 is '└'
UPLEFT    = chr(9496)  # Character 9496 is '┘'

TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2:'blue', 3:'yellow', 4:'cyan', 5:'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND, 3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'

def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()
    print('Do you want to play in colorblind mode? Y/N')
    response = input('> ')
    if response.upper().startswith('Y'):
        displayMode = SHAPE_MODE
    else:
        displayMode = COLOR_MODE

    gameBoard = getNewBoard()
    movesLeft = MOVES_PER_GAME

    while True:  # Main game loop.
        displayBoard(gameBoard, displayMode)

        print('Moves left:', movesLeft)
        playerMove = askForPlayerMove(displayMode)
        changeTile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if hasWon(gameBoard):
            displayBoard(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            displayBoard(gameBoard, displayMode)
            print('You have run out of moves!')
            break



























