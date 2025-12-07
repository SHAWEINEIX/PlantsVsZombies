from data.src.object import *

class Squash(Object):
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = "squash" # 设置植物类型为倭瓜
        self.game = game  # 保存游戏引用
        super().__init__(game.screen, settings[self.plantType]["path"], settings[self.plantType]["size"], settings[self.plantType]["imageCount"], self.plantType)  # 调用父类初始化函数，传入屏幕对象和设置参数
        self.pos = list(pos)
        self.pos[0] += settings["game"]["gridPlantPos"][self.plantType][0]
        self.pos[1] += settings["game"]["gridPlantPos"][self.plantType][1]
        self.updateGrid(self.pos)
        self.grid[0] += 1
        self.grid[1] += 2
        self.state = "Idle"
        self.delete = 0
        self.Todelete = 0
        self.attackPosX = None
        self.attackZombie = None
        self.TodeleteTime = 0
    
    def run(self):
        if not self.Todelete and not self.delete:
            self.update()
        if self.Todelete:
            self.TodeleteTime += 1
            if self.TodeleteTime >= settings[self.plantType]["deleteTime"]:
                self.delete = 1
        if self.attackPosX != None:
            if self.pos[0] < self.attackPosX:
                self.pos[0] += 1
            elif self.pos[0] > self.attackPosX:
                self.pos[0] -= 1
        if self.state == "Attack" and self.imageIndex == self.imageCount:
            self.Todelete = 1
        if self.state == "Attack" and self.imageIndex == self.imageCount - 1:
            self.game.game.AttackZombie(self.attackZombie)
        self.draw()