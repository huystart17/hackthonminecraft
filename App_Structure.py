class Structure:
    def __init__(self, mc, x, y, z, filename):
        self.mc = mc
        self.x = x
        self.y = y
        self.z = z
        self.filename = filename
        self.introduce_text = "This is famous building"
        self.tele_in_point = {"x": x, "y": y, "z": z}
        self.tele_out_point = {"x": x, "y": y, "z": z}
        pass

    def paste(self):
        mc = self.mc
        x = self.x
        y = self.y
        z = self.z
        filename = self.filename
        house = open(filename, 'r')
        blocks = house.read().split(',')
        for block in blocks:
            if block != '':
                dt = block.split(':')
                # xử lý lưu block teleport
                if int(dt[3]) == 201:
                    self.tele_in_point["x"] = x + int(dt[0])
                    self.tele_in_point["y"] = y + int(dt[0]) + 1
                    self.tele_in_point["z"] = z + int(dt[0])
                if int(dt[3]) == 202:
                    self.tele_out_point["x"] = x + int(dt[0])
                    self.tele_out_point["y"] = y + int(dt[0]) + 1
                    self.tele_out_point["z"] = z + int(dt[0])
                #
                mc.setBlock(
                    x + int(dt[0]),
                    y + int(dt[1]),
                    z + int(dt[2]),
                    int(dt[3]),
                    int(dt[4]),
                )

    def introduce(self):
        mc = self.mc
        mc.postToChat(self.introduce_text)
        pass

    def player_inside(self, id):
        pass

    def tele_in(self, id):
        pass

    def tele_out(self):
        pass
