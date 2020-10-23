from pygame.locals import *
from parameter import *



class Button:
    def __init__(self, game):
        self.screen = game.screen
        self.square = game.model.square
        self.win = game.model.win
        self.piece_list = game.model.piece_list
        self.pos0 = (checkerboard_range[0], checkerboard_range[1],
                     checkerboard_range[0] + checkerboard_range[2],
                     checkerboard_range[1] + checkerboard_range[3])  # (起始坐标pos_x, pos_y，终点坐标)
        self.step = game.model.step
        self.b = -1  # 是否选中要移动的黑色棋子-1:一步都没走 0：该走还没走 1：选中要走的棋子
        self.r = -1  # 是否选中要移动的红色棋子-1:一步都没走 0：该走还没走 1：选中要走的棋子
        self.b_rank = [[], []]  # 记录棋子移动的起点和终点
        self.r_rank = [[], []]  # 记录棋子移动的起点和终点
        pass

    def action(self, events):
        self.show_move()
        point_x, point_y = pygame.mouse.get_pos()
        if self.pos0[0] < point_x < self.pos0[2] and self.pos0[1] < point_y < self.pos0[3]:  # 鼠标是否在棋盘上
            n = (point_x - self.pos0[0]) // square_size[0]
            m = (point_y - self.pos0[1]) // square_size[1]
            x = self.pos0[0] + n * square_size[0]
            y = self.pos0[1] + m * square_size[1]
            self.screen.blit(self.mark, (x, y))  # 显示光标
            for event in events:  # 放置棋子
                if event.type == MOUSEBUTTONUP:
                    if self.step[0] == 0:  # 黑棋走
                        if self.b != 1:
                            if self.square[m][n] == 0:
                                self.b = 1
                                self.b_rank[0] = [m, n]
                        else:
                            self.b_rank[1] = [m, n]
                            for piece in self.piece_list:
                                if piece.rank == self.b_rank[0]:
                                    piece.move(self.square, self.b_rank[1], self.win, self.step, self.piece_list)
                                    self.b = 0


                    else:  # 红棋走
                        if self.r != 1:
                            if self.square[m][n] == 1:
                                self.r = 1
                                self.r_rank[0] = [m, n]
                        else:
                            self.r_rank[1] = [m, n]
                            for piece in self.piece_list:
                                if piece.rank == self.r_rank[0]:
                                    piece.move(self.square, self.r_rank[1], self.win, self.step, self.piece_list)
                                    self.r = 0
                                    break

                        pass
                    break

        pass

    def show_move(self):  # 显示棋子移动路径
        if self.step[0] == 1:
            self.mark = im_r_mark
        else:
            self.mark = im_b_mark

        if self.step[0] == 0:
            if self.r != -1:
                # 显示红色棋子移动起始位置光标
                rank = self.r_rank[0]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_r_mark, (x, y))
                # 显示红色棋子移动终点位置光标
                rank = self.r_rank[1]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_r_mark, (x, y))
            if self.b == 1:
                # 显示将要移动的黑色棋子位置光标
                rank = self.b_rank[0]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_b_mark, (x, y))
        elif self.step[0] == 1:
            if self.b != -1:
                # 显示黑色棋子移动起始位置光标
                rank = self.b_rank[0]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_b_mark, (x, y))
                # 显示黑色棋子移动终点位置光标
                rank = self.b_rank[1]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_b_mark, (x, y))
            if self.r == 1:
                # 显示将要移动的红色棋子位置光标
                rank = self.r_rank[0]
                m = rank[0]
                n = rank[1]
                x = self.pos0[0] + n * square_size[0]
                y = self.pos0[1] + m * square_size[1]
                self.screen.blit(im_r_mark, (x, y))