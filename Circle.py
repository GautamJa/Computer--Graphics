import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bresenham's/ Line Drawing Algorithm")

# Colors
WHITE = (255, 255, 255)
BLACK = (0,100,200)


# Function to draw a circle using DDA algorithm
def draw_circle(r,xc,yc):
    x=0
    y=r
    d=1-r
    while(x<=y):
        screen.set_at((round(x+xc), round(y+yc)),"RED")
        screen.set_at((round(y+yc), round(x+xc)), "BLUE")
        screen.set_at((round(x+xc), round(-y+yc)), "GREEN")
        screen.set_at((round(y+yc), round(-x+xc)), "PURPLE")
        screen.set_at((round(-y+yc), round(-x+xc)), "CYAN")       
        screen.set_at((round(-x+xc), round(-y+yc)), WHITE)
        screen.set_at((round(-x+xc), round(y+yc)), "ORANGE")
        screen.set_at((round(-y+yc), round(x+xc)), "RED")
        x=x+1
        if(d<0):
            y=y
            d=d+2*x+1
        else:
            y=y-1
            d=d+2*x-2*y+1
# Main loop
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

       

        # Draw a square using Bresenham's algorithm
        draw_circle(100,200, 200)

     
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()