import mcpi
import turtle

import time
from mcpi import minecraft
from mcpi import vec3
mc = minecraft.Minecraft.create("10.15.0.119")

sc = turtle.Screen()

ids = []
for plid in mc.getPlayerEntityIds():
    ids.append({"id" : plid, "turtle" : turtle.Turtle() })
for pl in ids :
    pl['turtle'].penup()

while True :
    time.sleep(1)
    for pl in ids :
        pl['turtle'].clear()
        x,y,z = mc.entity.getTilePos(pl['id'])
        pl['turtle'].setpos(x,z)
        pl['turtle'].write('{},{}'.format(x,z),font=("Arial",15, "normal"))



sc.mainloop()
