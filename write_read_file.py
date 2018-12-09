house = open('structures/house.csv', 'w')

print ("{}".format(house.writable()))
house.write("1")
# house.write("hekk")
# print(house.read().split('\n'))

house.close()
#GHi một 1 file là hello.csv
#Viết 1 dòng là "hello"
#đóng file
#và mở lại
#in nội dung bên trong file ra