import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+50, pos.y+50, pos.z+50, block.AIR.id)
pos = mc.player.getTilePos()
size = int(input("size of area to clear? "))
mc.setBlocks(pos.x, pos.y, pos.z, pos.x+size, pos.y+size, pos.z+size, block.AIR.id)