import pygame as pg
import sys
pg.init()

screen = pg.display.set_mode((1000, 1000))


def printT(tb):

    #printa as linhas
    x = 35
    y = 35
    
    for i in range(16):
        #-1 para corrigir os cantos
        start_pos = (x - 1 , y)

        # + 3 para corrigir
        end_pos = (start_pos[0] + 62*15 + 3 , start_pos[1])
        pg.draw.line(screen, (0, 0, 0), start_pos, end_pos, 4)

        y += 62

    x = 35
    y = 35

    for i in range(16):
        start_pos = (x, y)
        
        end_pos = (start_pos[0], start_pos[1] + 62*15)
        pg.draw.line(screen, (0, 0, 0), start_pos, end_pos, 4)
        
        x += 62
    #-----------------------------------------------------------
    #printa pecas:
    for i in range(len(tb)):
        for j in range(len(tb)):
            if tb[i][j] == 1:
                
                pg.draw.circle(screen, (255, 255, 255), ((i+1)*62+35-31, (j+1)*62+35-31), 22)

            elif tb[i][j] == 2:

                pg.draw.circle(screen, (0, 0, 0), ((i+1)*62+35-31, (j+1)*62+35-31), 22)        

                
                
def step(tb, pos):
    pass


def game():

    #iniciando tabuleiro
    gomoku = [0] * 15
    for i in range(len(gomoku)):
        gomoku[i] = [0] * 15

    

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
        
        screen.fill((245, 66, 90))

        printT(gomoku)        


        pg.display.flip()


game()