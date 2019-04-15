import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x == 5 and pos.z == -14:
        mc.postToChat("welcome home")