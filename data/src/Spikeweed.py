from data.src.object import *

class Spikeweed(Object):
    def __init__(self, game, pos):  # 初始化函数
        self.plantType = 'spikeweed'
        self.game = game
        super().__init__(game.screen, settings['spikeweed']['path'], settings['spikeweed']['size'], settings['spikeweed']['imageCount'], self.plantType)  # 调用父类初始化函数
        self.pos = list(pos)  # 保存nut位置
        self.pos[0] += settings['game']['gridPlantPos'][self.plantType][0]
        self.pos[1] += settings['game']['gridPlantPos'][self.plantType][1]
        self.updateGrid(self.pos)

    def run(self):  # 运行函数
        self.update()  # 更新图片
        self.draw()  # 绘制图片