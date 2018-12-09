from mcpi import minecraft
from mcpi import vec3 
Vec3 = vec3.Vec3
mc = minecraft.Minecraft.create("10.15.0.211")
from minecraftstuff import *

mc.postToChat("hello")

myid = mc.getPlayerEntityId('huyhuy17')
mc.entity.setPos(myid,120,150,120)
mypos = mc.entity.getPos(myid)

# for id in mc.getPlayerEntityIds():
#     mc.entity.setPos(id, mypos.x,mypos.y,mypos.z)
tt = MinecraftTurtle(mc,Vec3(mypos.x,mypos.y,mypos.z))
tt.pendown()
tt.speed(0)

for k in range (4):
    for j in range (4):
        for i in range(10):
            tt.forward(1)
        tt.left(90)
    tt.sety(tt.position.y +1)
for i in range (5):
    tt.penup()
    tt.forward(i)
    tt.pendown()
    tt.forward(10 -i *2)
    tt.penup()
    tt.sety(tt.position.y +1)
    tt.backward(10 -i)
#Xây 1 bức tường
#Xây 1 khối vuông rỗng
#Xây hình tam giác và đặt nó trên khối vuông vừa xây

