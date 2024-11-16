import pygame
import random

# Define conditions for drawing the screen and grid
LINE_WIDTH = 1
BOARD_ROWS = 16
BOARD_COLS = 20
LINE_COLOR = "dark blue"
SQUARE_SIZE = 32
WIDTH = 640
HEIGHT = 512
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Function to draw the 3x3 grid
def draw_grid():
    # Draw horizontal lines to separate the screen into a 3x3 grid
    for i in range(1, BOARD_ROWS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (0, i * SQUARE_SIZE),
            (WIDTH, i * SQUARE_SIZE),
            LINE_WIDTH
        )

    # Draw vertical lines to separate the screen
    for i in range(1, BOARD_COLS):
        pygame.draw.line(
            screen,
            LINE_COLOR,
            (i * SQUARE_SIZE, 0),
            (i * SQUARE_SIZE, HEIGHT),
            LINE_WIDTH
        )

# Function to select a random row and column to be called so that the image goes to a random square
def random_square():
    rand_row = random.randint(0, BOARD_ROWS - 1)
    rand_col = random.randint(0, BOARD_COLS - 1)
    return rand_row, rand_col

def main():
    try:
        pygame.init()
        mole_image = pygame.image.load("mole.png")
        # Set the initial starting position of the mole to the top-left square
        mole_row, mole_col = 0, 0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # Get the x and y coordinates of the mouse when clicked
                    x, y = event.pos
                    # Calculate the row value by taking the floor division of the y coordinate from the square size
                    row = y // SQUARE_SIZE
                    # Calculate the column value by taking the floor division of the x coordinate from the square size
                    col = x // SQUARE_SIZE

                    # If the coordinates of the click is the same as the coordinates of the image, that means the mole
                    # image has been clicked. If so, the image has to be set to a new row and column, so the
                    # random_square() function is called
                    if row == mole_row and col == mole_col:
                        mole_row, mole_col = random_square()

            screen.fill("light green")
            draw_grid()

            # Sets the x position of the mole to the column index multiplied by the size of each square
            mole_x = mole_col * SQUARE_SIZE
            # Sets the y position of the mole to the row index multiplied by the size of each square
            mole_y = mole_row * SQUARE_SIZE
            # Sets the mole image to the calculated (mole_x, mole_y) position
            screen.blit(mole_image, mole_image.get_rect(topleft = (mole_x, mole_y)))

            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()