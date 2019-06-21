import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
FILENAME = "tree.csv"
SIZEX = 5
SIZEY = 5
SIZEZ = 5
def scan3D(filename, originx, originy, originz):
    f = open(filename, "w")
    f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
    for y in range(SIZEY):
        f.write("\n")
        for x in range(SIZEX):
            line = ""
            for z in range(SIZEZ):
                blockid = mc.getBlock(originx+x, originy+y, originz+z)
                if line != "":
                    line = line + ","
            line = line + str(blockid)
        f.write(line + "\n")
    f.close()
pos = mc.player.getTilePos()
scan3D(FILENAME, pos.x-(SIZEX/2), pos.y, pos.z-(SIZEZ/2) )