import  pygame

pygame.init()

screen_size = (800, 480)#显示画面尺寸
square_size = (40, 40)#棋盘方格大小
piece_size = square_size[0] // 2#棋子半径尺寸
checkerboard_size = (360, 400) #棋盘大小

bg_color = (200, 200, 200)

checkerboard_pos = ((screen_size[1] - checkerboard_size[1]) // 2, (screen_size[1] - checkerboard_size[1]) // 2)#棋盘坐标
guide_pos = (screen_size[1], screen_size[1] // 10)
result_pos = (screen_size[1], screen_size[1] * 8 // 10)


checkerboard_range = (checkerboard_pos[0], checkerboard_pos[1], checkerboard_size[0], checkerboard_size[1])#棋盘范围


font = pygame.font.SysFont("隶书", 48)
font_color = [(200, 0, 0), (60, 60, 60), (0, 0, 0), (200, 200, 200)]

im_checkerboard = pygame.image.load("picture/checkerboard.png")
im_b_mark = pygame.image.load("picture/bb.png")
im_r_mark = pygame.image.load("picture/rb.png")

