import time
from mcpi import minecraft
from mcpi import vec3

Vec3 = vec3.Vec3
mc = minecraft.Minecraft.create()
from minecraftstuff import *

time.sleep(0.5)
mc.postToChat("xin chao")
mc.postToChat('Ban co 3 lua chon')
mc.postToChat('1.xem thong tin')
mc.postToChat('2.di chuyen ben trong')
mc.postToChat('3.khong nhan tin nhan trong 10s nua')
while True:
    chatmsgs = mc.events.pollChatPosts()
    for msg in chatmsgs :
        if(msg.message =='1'):
            mc.postToChat("Gui {}, thong tin :".format(msg.entityId))
            mc.postToChat("Chung toi la tap doan to nhat qua dat")
            mc.clearAll()
