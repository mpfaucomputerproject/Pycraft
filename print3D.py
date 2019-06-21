import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
FILENAME = "object1.csv"
def print3D(filename, originx, originy, originz):
    f = open(filename, "r")
    lines = f.readlines()
    coords = lines[0].split(",")
    sizex = int(coords[0])
    sizey = int(coords[1])
    sizez = int(coords[2])
    lineidx = 1
    for y in range(sizey):
        mc.postToChat(str(y))
        lineidx = lineidx + 1
        
        for x in range(sizex):
            line = lines[lineidx]
            lineidx = lineidx + 1
            data = line.split(",")
            
            for z in range(sizez):
                blockid = int(data[z] )
                mc.setBlock(originx+x, originy+y, originz+z, blockid)

pos = mc.player.getTilePos()
print3D(FILENAME, pos.x+1, pos.y, pos.z+1)