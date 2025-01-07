
import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 1000, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's/ Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,100,200)


# Function to draw a Ellipse using DDA algorithm
def draw_Ellipse(xc,yc,rx,ry):
    
    x=0
    y=ry
    p1=ry*ry-rx*rx*ry+(1/4)*rx*rx
    # FOR REGION 1
    
    while(2*ry*ry*x<=2*rx*rx*y):
        screen.set_at((round(x+xc), round(y+yc)),"RED")
        screen.set_at((round(x+xc), round(-y+yc)),"RED")
        screen.set_at((round(-x+xc), round(y+yc)),"RED")
        screen.set_at((round(-x+xc), round(-y+yc)),"RED")
        
        if(p1<0):
            x=x+1
            y=y
            p1=p1+2*ry*ry*x+ry*ry
        else:
            x=x+1
            y=y-1
            
            p1=p1+2*ry*ry*x-2*rx*rx*y+ry*ry
            
    #FOR REGION 2
    p2=(ry*ry*(x+0.5)*(x+0.5)+rx*rx*((y-1)*(y-1))-rx*rx*ry*ry)
    while(y!=0):
        screen.set_at((round(x+xc), round(y+yc)),"RED")
        screen.set_at((round(x+xc), round(-y+yc)),"RED")
        screen.set_at((round(-x+xc), round(y+yc)),"RED")
        screen.set_at((round(-x+xc), round(-y+yc)),"RED")
        if(p2>0):
            x=x
            y=y-1
            p2=p2-2*rx*rx*y+rx*rx
        else:
            x=x+1
            y=y-1
            p2=(p2+2*ry*ry*x-2*rx*rx*y+rx*rx)
        


    

# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       

        # Draw a square using Bresenham's algorithm
        draw_Ellipse(500,350,200,100)
        draw_Ellipse(500,350,250,150)
        draw_Ellipse(500,350,300,200)
        draw_Ellipse(500,350,350,250)
        draw_Ellipse(500,350,490,390)
        draw_Ellipse(300,350,20,20)
        draw_Ellipse(500,350,50,50)
        draw_Ellipse(305,450,25,25)
        draw_Ellipse(200,350,30,30)
        draw_Ellipse(220,200,50,50)
        draw_Ellipse(220,650,80,80)



     
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()