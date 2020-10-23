import pygame

#车
class Jv:
    def __init__(self, id, rank):
        self.id = id
        self.rank = rank
        self.no = 1
        if self.id == 0:
            self.img = pygame.image.load("picture/bc.png")
        else:
            self.img = pygame.image.load("picture/rc.png")

    def move(self, square, rank, win, step, piece_list):
        #判断是否能走
        a = rank[0] - self.rank[0]
        b = rank[1] - self.rank[1]
        if self.rank != rank and a * b == 0 and square[rank[0]][rank[1]] != self.id:
            c = 1
            if self.rank[0] == rank[0]:
                if self.rank[1] > rank[1]:
                    a = rank[1] + 1
                    b = self.rank[1]
                else:
                    a = self.rank[1] + 1
                    b = rank[1]
                for i in range(a, b):
                    if square[rank[0]][i] != -1:
                        c = 0
                        break
            else:
                if self.rank[0] > rank[0]:
                    a = rank[0] + 1
                    b = self.rank[0]
                else:
                    a = self.rank[0] + 1
                    b = rank[0]
                for i in range(a, b):
                    if square[i][rank[0]] != -1:
                        c = 0
                        break
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