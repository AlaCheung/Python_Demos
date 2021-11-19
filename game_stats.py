# -*- codeing = utf-8 -*-
# @Time : 2021/11/19 14:31
# @Author : Lucas Cheung
# @File : game_stats.py
# @Software : PyCharm

class GameStats:
    """跟踪游戏的统计信息"""

    def __init__(self, ai_game):
        """初始化统计信息"""
        self.setting = ai_game.setting
        self.reset_stats()

        # 游戏刚启动时处于非活动状态
        self.game_active = False

        # 任何情况下都不能重置最高得分
        self.high_score = 0

    def reset_stats(self):
        """初始化在游戏运行期间可能变化的统计信息"""
        self.ships_left = self.setting.ship_limit
        self.score = 0
        self.level = 1
