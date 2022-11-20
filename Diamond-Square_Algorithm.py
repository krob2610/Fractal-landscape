import numpy as np
import random
from mayavi import mlab

def diamond_board(lvl, glued, initial_corners = None):
    size = (2**lvl)
    board  = np.zeros((size+1,  size+1))
    randomness = 2**lvl-1
    if initial_corners != None:
        board[0][0] = initial_corners[0]
        board[0][-1] = initial_corners[1]
        board[-1][0] = initial_corners[2]
        board[-1][-1] = initial_corners[3]

    tile_size = size
    while tile_size > 1:
        half_tile_size = tile_size // 2

        #mid avg
        for x in range(0, size - 1, tile_size):
            for y in range(0, size - 1, tile_size):
                cornerSum = board[x][y] + board[x + tile_size][y] + board[x][y + tile_size] + board[x + tile_size][y + tile_size]

                avg = cornerSum / 4
                avg += random.randint(-randomness, randomness)

                board[x + half_tile_size][y + half_tile_size] = avg

        #in line avg neig
        for x in range(0, size, half_tile_size):
            for y in range((x + half_tile_size) % tile_size, size, tile_size):
                avg = board[(x - half_tile_size + size) % size][y] + \
                      board[(x + half_tile_size) % size][y] + \
                      board[x][(y + half_tile_size) % size] + \
                      board[x][(y - half_tile_size + size) % size]

                avg /= 4.0
                avg += random.randint(-randomness, randomness)

                board[x][y] = avg

                # jesli mapa ma byc sklejona
                if glued:
                    if x == 0:
                        board[size][y] = avg
                    if y == 0:
                        board[x][size] = avg

            # reduce the randomness in each pass, making sure it never gets to 0
        randomness = max(randomness // 2, 1)
        tile_size //= 2
    return board
#surf = mlab.surf(diamond_board(10, glued= True, initial_corners = [1,2,3,4]), colormap='gist_earth', warp_scale='auto')
board = diamond_board(10, glued= True)
surf = mlab.surf(board, colormap='gist_earth', warp_scale='auto')
#mlab.show()
mlab.imshow(board, colormap='gist_earth')
mlab.show()
