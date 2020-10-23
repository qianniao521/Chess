from model import *
from parameter import *
from button import *
import sys

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(screen_size)
        self.clock = pygame.time.Clock()
        pass

    #游戏开始
    def game_start(self):
        self.model = Model()
        self.button = Button(self)

        while True:
            self.clock.tick(60)
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
            self.load_checkerboard()
            self.load_piece(self.model.piece_list)
            self.load_guide()
            if self.model.win[0] == -1:
                self.button.action(events)
            else:
                self.load_win()
            pygame.display.update()


        pass

    def load_checkerboard(self):
        self.screen.fill(bg_color)
        self.screen.blit(im_checkerboard, checkerboard_pos)

    def load_piece(self, piece_list):
        for piece in piece_list:
            m = piece.rank[0]
            n = piece.rank[1]
            x = checkerboard_pos[0] + n * square_size[0]
            y = checkerboard_pos[1] + m * square_size[1]
            self.screen.blit(piece.img, (x, y))
        pass

    def load_guide(self):
        if self.model.step[0] == 0:
            surface = font.render("黑棋走！", False, font_color[2])
            self.screen.blit(surface, guide_pos)
        else:
            surface = font.render("红棋走！", False, font_color[2])
            self.screen.blit(surface, guide_pos)
        pass

    def load_win(self):
        if self.model.win[0] == 0:
            surface = font.render("黑棋胜！", False, font_color[0])
            self.screen.blit(surface, result_pos)
        else:
            surface = font.render("红棋胜！", False, font_color[0])
            self.screen.blit(surface, result_pos)
        pass


if __name__ == '__main__':
    game = Game()
    game.game_start()