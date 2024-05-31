import pygame


pygame.init()
width,height=1000,400
font = pygame.font.Font('freesansbold.ttf', width//70)

screen=pygame.display.set_mode((width,height))
clock=pygame.time.Clock()
picker=pygame.image.load("spectrum.jpg")
picker = pygame.transform.scale(picker, (height,height))


def new_color(x,y):
    return screen.get_at((x,y))

def main():
    rtext="0"
    gtext="0"
    btext="0"

    ccc=(0,0,0)
    running=True
    while running:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            if pygame.mouse.get_pressed()[0]:
                x,y=pygame.mouse.get_pos()
                if 0<=x<=height and 0<=y<=height:
                    ccc=new_color(x,y)
                    rtext,gtext,btext=(str(ccc[0]),str(ccc[1]),str(ccc[2]))
        screen.fill((255,255,255))
        screen.blit(picker,(0,0))


        top_left=(width-width/8,0)
        text1 = font.render(btext, True, (0,0,0), (255,255,255))
        text2 = font.render(gtext, True, (0,0,0), (255,255,255))
        text3 = font.render(rtext, True, (0,0,0), (255,255,255))
        pygame.draw.rect(screen,ccc,(*top_left,width/8,height))

        screen.blit(text1,((width-width/8-width//25)-width//200,height//2-255//2+265))
        pygame.draw.line(screen,"black",(width-width/8-width//25,height//2-255//2),(width-width/8-width//25,height//2-255//2+255))

        screen.blit(text2,((width-width/8-2*(width//25))-width//200,height//2-255//2+265))
        pygame.draw.line(screen,"black",(width-width/8-2*(width//25),height//2-255//2),(width-width/8-2*(width//25),height//2-255//2+255))

        screen.blit(text3,((width-width/8-3*(width//25))-width//200,height//2-255//2+265))
        pygame.draw.line(screen,"black",(width-width/8-3*(width//25),height//2-255//2),(width-width/8-3*(width//25),height//2-255//2+255))

        

        pygame.display.update()
    pygame.quit()

main()

