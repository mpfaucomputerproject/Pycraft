import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

mc = minecraft.Minecraft.create()

RANGE = 5
treasures = []
def clearSpace():
    pos = mc.player.getTilePos()
    mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+50, block.AIR.id)

def placeTreasure():
    global treasures
    pos = mc.player.getTilePos()
    for treasure in range(5):
        treasure_x = random.randint(pos.x,  pos.x+RANGE)
        treasure_y = random.randint(pos.y, pos.y+RANGE)
        treasure_z = random.randint(pos.z,  pos.z+RANGE)
        treasures.append([treasure_x, treasure_y, treasure_z])
        mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)

def checkHit():
    global treasures

    events = mc.events.pollBlockHits()

    for coordinate in treasures:
        for e in events:
            pos = e.pos
            if pos.x == coordinate[0] and pos.y == coordinate[1] and pos.z == coordinate[2]:
                mc.postToChat("Treasure Found!")
                mc.setBlock(coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
                coordinate[0] = None
                coordinate[1] = None
                coordinate[2] = None
                treasures.pop(treasures.index(coordinate))
                mc.postToChat(str(len(treasures)) + "blocks left.")
clearSpace()
placeTreasure()
while len(treasures) > 0:
    checkHit()
mc.postToChat("Finished")