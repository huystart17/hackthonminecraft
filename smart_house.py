from mcpi import minecraft
from mcpi import vec3

Vec3 = vec3.Vec3
mc = minecraft.Minecraft.create("10.15.0.119")

#how to move everybody to one point
def make_ground ():    
    ids = mc.getPlayerEntityIds()
    x,y,z =0,80,0
    mc.postToChat("all go into one")
    #
    mc.setBlocks (x,y,z  ,x + 50 ,y + 50 ,z+50,0)
    mc.setBlocks (x ,y,z, x+50,y+2,z +50,1)
    y = y +2
    for id in ids :
        mc.entity.setPos(id,x+10,y,z+10)


def make_house ():
    x ,y,z  = 0,80,0
    mc.setBlocks (x,y,z  ,x + 15 ,y + 15 ,z+15,0)
    mc.setBlocks (x ,y,z, x+15,y,z +15,1)
    w =8
    h =8
    mc.setBlocks(x,y,z, x + w, y + h , z +w ,17,1)
    mc.setBlocks(x + 1 ,y + 1,z + 1 , x + w -1, y + h - 1, z +w -1 ,0)
    mc.setBlock(x + w // 2 ,y,z , 64 )
make_house () 
