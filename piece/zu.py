import pygame


# 卒
class Zu:
    def __init__(self, id, rank):
        self.id = id
        self.rank = rank
        self.no = 6
        if self.id == 0:
            self.img = pygame.image.load("picture/bz.png")
        else:
            self.img = pygame.image.load("picture/rz.png")

    def move(self, square, rank, win, step, piece_list):
        for i in piece_list:
            if i.no == 0:
                if i.id == self.id:
                    if i.rank[0] > 4:
                        self.d = 4
                    else:
                        self.d = 5
        # 判断是否能走
        a = rank[0] - self.rank[0]
        b = rank[1] - self.rank[1]
        if a * a + b * b == 1 and square[rank[0]][rank[1]] != self.id:
            c = 1
            if self.d == 4:
                if a == 1 or (self.rank[0] > 4 and a != -1):
                    c = 0
            else:
                if a == -1 or (self.rank[0] < 5 and a != 1):
                    c = 0

            # 如能走执行走操作
            if c == 1:
                if square[rank[0]][rank[1]] != -1:
                    for i in piece_list:
                        if i.rank == rank:
                            piece_list.remove(i)
                            if i.no == 0:
                                win[0] = self.id
                            break
                square[self.rank[0]][self.rank[1]] = -1
                square[rank[0]][rank[1]] = self.id
                self.rank = rank
                step[0] = (step[0] + 1) % 2
            pass
