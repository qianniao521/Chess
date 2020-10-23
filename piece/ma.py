import pygame


#马
class Ma:
    def __init__(self, id, rank):
        self.id = id
        self.rank = rank
        self.no = 2
        if self.id == 0:
            self.img = pygame.image.load("picture/bm.png")
        else:
            self.img = pygame.image.load("picture/rm.png")

    def move(self, square, rank, win, step, piece_list):
        #判断是否能走
        a = rank[0] - self.rank[0]
        b = rank[1] - self.rank[1]
        if a ** 2 + b ** 2 == 5 and square[rank[0]][rank[1]] != self.id:
            c = 1
            if a == 2 or a == -2:
                if square[self.rank[0] + a // 2][self.rank[1]] != -1:
                    c = 0
            else:
                if square[self.rank[0]][self.rank[1] + b // 2] != -1:
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