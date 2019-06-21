import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
diamond_pos = mc.player.getTilePos()
diamond_pos.x = diamond_pos.x + 1
mc.setBlock(diamond_pos.x, diamond_pos.y, diamond_pos.z, block.DIAMOND_BLOCK.id)
def checkHit():
    global score
    global treasure_x
    events = mc.events.pollBlockHits()
    for e in events:
        pos = e.pos
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            mc.postToChat("HIT")
            score = score + 10
            mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
            treasure_x = None
while True:
    time.sleep(1)
    checkHit()
def checkHit():
    global score
    global treasure_x
TIMEOUT = 10
timer = TIMEOUT
def homingBeacon():
    global timer
    if treasure_x != None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT
            pos = mc.player.getTilePos()
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            diff = diffx + diffy + diffz
            mc.postToChat("score:" + str(score) + " treasure:" + str(diff))