import time
from mcpi import minecraft
from mcpi import vec3

Vec3 = vec3.Vec3
mc = minecraft.Minecraft.create("10.15.0.119")


def setBlocksToFile(x, y, z, x1, y1, z1, filename):
    blocks = ""
    _x, _y, _z = x1 - x, y1 - y, z1 - z
    r1 = range(0, _x)
    r2 = range(0, _y)
    r3 = range(0, _z)
    if (_x < 0):
        r1 = range(_x, 0)
    if (_y < 0):
        r2 = range(_y, 0)
    if (_z < 0):
        r3 = range(_z, 0)
    for a in r1:
        for b in r2:
            for c in r3:
                block = mc.getBlockWithData(x + a, y + b, z + c)
                blocks += "{}:{}:{}:{}:{},".format(a, b, c, block.id, block.data)
    house = open(filename, 'w+')
    house.write(blocks)
    house.close()


def printBlocksFromFile(x, y, z, filename):
    house = open(filename, 'r')
    blocks = house.read().split(',')
    for block in blocks:
        if block != '':
            dt = block.split(':')
            mc.setBlock(
                x + int(dt[0]),
                y + int(dt[1]),
                z + int(dt[2]),
                int(dt[3]),
                int(dt[4]),
            )
# x,y,z = 0 ,80 ,0
# for i in range (10):
#     x = x + 10
#     printBlocksFromFile(x,y,z ,"thang_house.csv")
#     mc.entity.setPos(mc.getPlayerEntityId('huyhuy17'), x,y,z)
#     mc.postToChat("Xay xong")
while True:
    time.sleep(1)
    x,y,z =  mc.entity.getPos(mc.getPlayerEntityId('huyhuy17'))
    bl  = mc.getBlock(x,y-1,z)
    if bl ==12 :
        mc.entity.setPos(mc.getPlayerEntityId('huyhuy17'), x,y-3,z )