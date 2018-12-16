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
        mc.postToChat("Copy {}/{}".format(a, r1))
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


# telefrom = [{x,y,z,202]
# teleto = [{x,y,z,201]
# def teleport(x1,y1,z1,x2,y2,z2,blockid,blockdata):


setBlocksToFile(128, 98, 84, 149, 106, 63, 'hello.csv')
# printBlocksFromFile(160,101,65,'hello.csv')
