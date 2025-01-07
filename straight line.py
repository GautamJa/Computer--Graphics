import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("bresh Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to draw a line using DDA algorithm
def draw_line_bres(x1, y1, x2, y2):
       dx=x2-x1
       dy=y2-y1
       x=x1
       y=y1
       if x2>x1:
            lx=1
       else :
            lx=-1
       if y2>y1:
            ly=1
       else:
            ly=-1
       if dx>dy:
          P= 2*dy-dx
          while (not(x==x2)):
            if p<0 :
                x=x+lx
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
            screen.set_at((round(x), round(y)), WHITE)    
       else :
           p=2*dx-2*dy
           while (not(y==y2)):
                if p<0:
                 y=y+ly
                 p=p+2*dx
                else :
                 x=x+lx
                 y=y+ly
                 p=p+2*dx-2*dy    
      

def sca(x1,y1,x2,y2,Sx,Sy):
    x3=x1*Sx
    x4=x2*Sx
    y3=y1*Sy
    y4=y2*Sy
    dx=x4-x3
    dy=y4-y3
    x=x3
    y=y3
    if x4>x3:
        lx=1
    else :
        lx=-1
    if y4>y3:
        ly=1
    else:
        ly=-1
    if dx>dy:
        p=2*dy-dx
        while (not(x==x4)):
            if p<0:
                x=x+lx
                p=p+2*dy
            else:
                x=x+lx
                y=y+ly
                p=p+2*dy-2*dx
        screen.set_at((round(x), round(y)), WHITE)    
    else :
        p=2*dx-2*dy
        while (not(y==y4)):
            if p<0:
                y=y+ly
                p=p+2*dx
            else :
                x=x+lx
                y=y+ly
                p=p+2*dx-2*dy    
            screen.set_at((round(x), round(y)), WHITE)     




    


       
 
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Clear the screen
        screen.fill(BLACK)

        # Draw a line using DDA algorithm
        draw_line_bres(20,20 , 100, 100)
        sca(20,20 , 100, 100,1,2)

        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()

