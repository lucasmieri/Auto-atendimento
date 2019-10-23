import pygame
LCD_debug_mode = True

def init(chars,lines):
    global screen
    global myfont
    pygame.init()
    size = [12*chars,20*lines]
    screen= pygame.display.set_mode(size)
    pygame.display.set_caption("16x2 LCD")
    myfont = pygame.font.SysFont("monospace", 20)

def draw(args):
    i=0;
    global screen
    global myfont
    screen.fill((0,0,0))#erase screen contents
    while(i < len(args)):
        line= myfont.render(args[i], 2, (255,255,0))
        screen.blit(line, (0, 20*i))
        i+=1
    pygame.display.flip()

def lcd_write(first_line, second_line):
    '''Este método recebe 2 strings e escreve no display ou no simulador.(depende da variavel LCD_debug_mode)
    primeiro argumento: linha de cima
    segundo argumento: linha de baixo
    Este método não retorna nenhum valor'''

    global LCD_debug_mode
    if LCD_debug_mode == True:
        draw(["%s" %first_line,"%s" %second_line]) #draw the two lines passed as a list

init(16,2) # initialize a 16x2 display