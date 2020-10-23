import numpy as np
from piece.pieces import *

class Model:
    def __init__(self):
        self.piece_list = []
        self.win = [-1]
        self.step = [1]
        self.square = np.zeros((15, 15)) - 1

        # 黑棋
        self.piece_list.append(Jv(0, [0, 0]))
        self.piece_list.append(Jv(0, [0, 8]))
        self.piece_list.append(Ma(0, [0, 1]))
        self.piece_list.append(Ma(0, [0, 7]))
        self.piece_list.append(Xiang(0, [0, 2]))
        self.piece_list.append(Xiang(0, [0, 6]))
        self.piece_list.append(Shi(0, [0, 3]))
        self.piece_list.append(Shi(0, [0, 5]))
        self.piece_list.append(Jiang(0, [0, 4]))
        self.piece_list.append(Pao(0, [2, 1]))
        self.piece_list.append(Pao(0, [2, 7]))
        self.piece_list.append(Zu(0, [3, 0]))
        self.piece_list.append(Zu(0, [3, 2]))
        self.piece_list.append(Zu(0, [3, 4]))
        self.piece_list.append(Zu(0, [3, 6]))
        self.piece_list.append(Zu(0, [3, 8]))
        # 红棋
        self.piece_list.append(Jv(1, [9, 0]))
        self.piece_list.append(Jv(1, [9, 8]))
        self.piece_list.append(Ma(1, [9, 1]))
        self.piece_list.append(Ma(1, [9, 7]))
        self.piece_list.append(Xiang(1, [9, 2]))
        self.piece_list.append(Xiang(1, [9, 6]))
        self.piece_list.append(Shi(1, [9, 3]))
        self.piece_list.append(Shi(1, [9, 5]))
        self.piece_list.append(Jiang(1, [9, 4]))
        self.piece_list.append(Pao(1, [7, 1]))
        self.piece_list.append(Pao(1, [7, 7]))
        self.piece_list.append(Zu(1, [6, 0]))
        self.piece_list.append(Zu(1, [6, 2]))
        self.piece_list.append(Zu(1, [6, 4]))
        self.piece_list.append(Zu(1, [6, 6]))
        self.piece_list.append(Zu(1, [6, 8]))

        for piece in self.piece_list:
            self.square[piece.rank[0]][piece.rank[1]] = piece.id
