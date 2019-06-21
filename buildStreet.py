import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
SIZE = 20
pos = mc.player.getTilePos()
x = pos.x+2
y = pos.y
z = pos.z
def house():
    midx = x + SIZE/2
    midy = y + SIZE/2
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    mc.setBlocks(x+1, y, z+1, x+SIZE-1, y+SIZE-1, z+SIZE-1, block.AIR.id)
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-1, y-1, z+SIZE-1, block.WOOL.id, 14)
house()
for h in range(5):
    house()
    x = x + SIZE