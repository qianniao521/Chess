import pygame



# 将
class Jiang:
    def __init__(self, id, rank):
        self.id = id
        self.rank = rank
        self.no = 0
        if self.id == 0:
            self.img = pygame.image.load("picture/bj.png")
        else:
            self.img = pygame.image.load("picture/rj.png")

    def move(self, square, rank, win, step, piece_list):
        # 判断是否能走
        a = rank[0] - self.rank[0]
        b = rank[1] - self.rank[1]
        if a * a + b * b == 1 and square[rank[0]][rank[1]] != self.id:
            c = 1
            if self.in_x(self.rank) and self.in_x(rank) == 0:
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
        elif self.rank != rank and b == 0 and square[rank[0]][rank[1]] == (self.id + 1) % 2:#对将
            for piece in piece_list:
                if piece.rank == rank and piece.no == 0:
                    c = 1
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
                    if c == 1:
                        win[0] = self.id
                        piece_list.remove(piece)
                        square[self.rank[0]][self.rank[1]] = -1
                        square[rank[0]][rank[1]] = self.id
                        self.rank = rank
                        step[0] = (step[0] + 1) % 2
                    break

            pass

    def in_x(self, rank):
        if (0 <= rank[0] <=2 or 7 <= rank[0] <= 9) and 3 <= rank[1] <= 5:
            return 1
        else:
            return 0