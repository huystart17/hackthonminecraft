from App_Structure import *
import time
from mcpi import minecraft
from mcpi import vec3

Vec3 = vec3.Vec3
mc = minecraft.Minecraft.create()
from minecraftstuff import *

mybuild = Structure(mc,140,101,103, 'thang_house.csv')
mybuild.introduce()
mybuild.paste()