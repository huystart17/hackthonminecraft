from mcpi import minecraft

mc = minecraft.Minecraft.create('10.15.0.18')
mc.postToChat("Hello")

# đưa người chơi đến khu vực xây dựng

# Khai báo toạ độ gốc xây công trình
root_x, root_z = 5, 5
root_x1, root_z1 = 150, 150
root_y = 50
root_y1 = 100
# Xoá block

# mc.setBlocks(root_x, root_y, root_z, root_x1, root_y1, root_z1, 0) #Chỉ chạy 1 lần
# Đặt nền
mc.setBlocks(root_x, root_y, root_z, root_x1, root_y + 2, root_z1, 35)

# set player's position to where we make contructions
m_id = mc.getPlayerEntityId('huyhuy17')
mc.entity.setPos(m_id, root_x + 6, root_y + 6, root_y + 6)

#Xây dựng căn nhà
# Toạ độ gốc của căn nhà đầu tiên
# Xác chiều cao và độ rộng của ngôi nhà
# độ rộng của công trình, cũng của vườn bao quanh nhà
# Dựng khối trước
# Làm rỗng căn phòng
# Đặt cửa


