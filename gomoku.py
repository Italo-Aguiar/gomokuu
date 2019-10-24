import pygame as pg
import sys
pg.init()

screen = pg.display.set_mode((1000, 1000))
screen.fill((245, 66, 90))

pg.display.set_caption("Gomoku")

font = pg.font.SysFont('Arial', 45)


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
    if tb[pos[0]][pos[1]] == 0:
        return True
    else:
        return False

def get_cell(pos):
    if pos[0] < 35 or pos[0] > 965 or pos[1] < 35 or pos[1] > 965:
        return False
    
    x = 35
    y = 35
    
    cellx = 20
    celly = 20

    for i in range(15):
        if pos[0] >= x and pos[0] < 62 * (i+1) + 35:
            cellx = i
        if pos[1] >= y and pos[1] < 62 * (i+1) + 35:
            celly = i

        x += 62
        y += 62
    
    return [cellx, celly]

def status(tb, turn, pos):
    #checa se matriz nao tem mais espacos vazios (deu empate):
    check = 0
    for i in range(len(tb)):
        for j in range(len(tb)):
            if tb[i][j] != 0:
                check += 1
    if check == 15*15:
        return 3
    
    #checa linha horizontal:
    countH = 0
    for i in range(pos[0], pos[0]+5):
        if i >= len(tb):
            break

        if tb[i][pos[1]] == tb[pos[0]][pos[1]]:
            countH += 1

        else:
            break

    for j in range(pos[0]-1, pos[0]-5, -1):
        if j < 0:
            break
        
        if tb[j][pos[1]] == tb[pos[0]][pos[1]]:
            countH +=1
        
        else:
            break
    
    #checa linha vertical:
    countV = 0
    for i in range(pos[1], pos[1] + 5):
        if i >= len(tb):
            break

        if tb[pos[0]][i] == tb[pos[0]][pos[1]]:
            countV +=1
        
        else:
            break

    for j in range(pos[1]-1, pos[1]-5, -1):
        if j < 0:
            break

        if tb[pos[0]][j] == tb[pos[0]][pos[1]]:
            countV += 1
        
        else:
            break

    #checa linha diagonal:
    countD = 0
    for i in range(5):
        if pos[0] + i >= len(tb) or pos[1] + i >= len(tb):
            break
    
        if tb[pos[0] + i][pos[1] + i] == tb[pos[0]][pos[1]]:
            countD += 1

        else:
            break
    
    for i in range(1, 5):
        if pos[0] + i >= len(tb) or pos[1] + i >= len(tb):
            break

        if tb[pos[0] - i][pos[1] - i] == tb[pos[0]][pos[1]]:
            countD += 1
        
        else:
            break

    #retorna vitorias ou continuar
    if countV == 5 or countH == 5 or countD == 5:
        if turn == 0:
            return 1
        elif turn == 1:
            return 2
    else:
        return 0
        


def game():
    continue_playing = True

    brancas_ganharam = False
    pretas_ganharam = False
    empatou = False

    turn = 2

    #iniciando tabuleiro
    gomoku = [0] * 15
    for i in range(len(gomoku)):
        gomoku[i] = [0] * 15

    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if continue_playing:
                if event.type == pg.MOUSEBUTTONUP:
                    mouse_pos = pg.mouse.get_pos()

                    pos = get_cell(mouse_pos)

                    if pos == False:
                        break
                    
                    cell = step(gomoku, pos)

                    if cell:
                        if turn % 2 == 0:
                            gomoku[pos[0]][pos[1]] = 1
                        elif turn % 2 == 1:
                            gomoku[pos[0]][pos[1]] = 2
                    
                        current_status = status(gomoku, turn % 2, pos)

                        if current_status == 1:
                            brancas_ganharam = True
                        elif current_status == 2:
                            pretas_ganharam = True
                        elif current_status == 3:
                            empatou = True    

                        turn += 1
       
        printT(gomoku)

        if brancas_ganharam:
            surface = font.render("Brancas Ganharam!", True, (255, 255, 255))#.get_rect().center = (500, 500)
            screen.fill((245, 66, 90))
            screen.blit(surface, (340, 440))
        elif pretas_ganharam:
            surface = font.render("Pretas Ganharam!", True, (255, 255, 255))#.get_rect().center = (500, 500)
            screen.fill((245, 66, 90))
            screen.blit(surface, (340, 440))
        elif empatou:
            surface = font.render("Empate!", True, (255, 255, 255))#.get_rect().center = (500, 500)
            screen.fill((245, 66, 90))
            screen.blit(surface, (340, 440))
            

        pg.display.flip()


game()