import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()

BOARD = []
PLAYER = 1
BOARD_BLOCK = block.STONE.id
P1_BLOCK = block.BRICK_BLOCK.id
P2_BLOCK = block.SANDSTONE.id
WINNER = False

def makeBoard():
    global BOARD

    for row in range(3):
        BOARD.append([])
        for column in range(3):
            BOARD[row].append(0)

def buildBoard():
    global BOARD, BOARD_BLOCK, P1_BLOCK, P2_BLOCK

    for row in range(3):
        for column in range(3):
            if BOARD[row][column] == 0:
                mc.setBlock(pos.x + column, pos.y+row, pos.z+2, BOARD_BLOCK)
            elif BOARD[row][column] == 1:
                mc.setBlock(pos.x + column, pos.y+row, pos.z+2, P1_BLOCK)
            elif BOARD[row][column] == -1:
                mc.setBlock(pos.x + column, pos.y+row, pos.z+2, P2_BLOCK)
            else:
                pass

def blockHit():
    global BOARD, PLAYER, P1_BLOCK, P2_BLOCK
    events = mc.events.pollBlockHits()
    for e in events:
        block_pos = e.pos

        for row in range(3):
            for column in range(3):
                if BOARD[row][column] == 0:
                    if block_pos.x == pos.x + column and block_pos.y == pos.y + row and block_pos.z == pos.z + 2:
                        if PLAYER == 1:
                            BOARD[row][column] = 1
                            PLAYER = 2
                        else:
                            BOARD[row][column] = -1
                            PLAYER = 1
            else:
                pass
        else:
            pass

def checkWin():
    global BOARD, WINNER
    for row in range(3):
        if BOARD[row][0] + BOARD[row][1] + BOARD[row][2] == 3:
            mc.postToChat("Player 1 wins.")
            WINNER = True
            pass
        if BOARD[row][0] + BOARD[row][1] + BOARD[row][2] == -3:
            mc.postToChat("Player 2 wins.")
            WINNER = True
            pass
    for column in range(3):
        if BOARD[0][column] + BOARD[1][column] + BOARD[2][column] == 3:
            mc.postToChat("Player 1 wins.")
            WINNER = True
            pass
        if BOARD[0][column] + BOARD[1][column] + BOARD[2][column] == -3:
            mc.postToChat("Player 2 wins.")
            WINNER = True
            pass
    if BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == 3:
        mc.postToChat ("Player 1 wins.")
        WINNER = True
        pass
    elif BOARD[0][0] + BOARD[1][1] + BOARD[2][2] == -3:
        mc.postToChat("Player 2 wins.")
        WINNER = True
        pass
    elif BOARD[0][2] + BOARD[1][1] + BOARD[2][0] == 3:
        mc.postToChat ("Player 1 wins.")
        WINNER = True
        pass
    elif BOARD[0][2] + BOARD[1][1] + BOARD[2][0] == -3:
        mc.postToChat ("Player 2 wins.")
        WINNER = True
        pass

makeBoard()
buildBoard()
while not WINNER:
    blockHit()
    checkWin()
    buildBoard()