import numpy as np
import random
from mayavi import mlab
def generate_board(lvl):
    size = (2 ** lvl)
    board = np.zeros((size + 1, size + 1))
    for i in range(size+1):
        for j in range(i+1):
            board[i][j] = 1
    #board[int(n/3):n][int(n/3):n] = 0
    return board, size

def generate_board_squ(lvl):
    size = (2 ** lvl)
    board = np.ones((size + 1, size + 1))
    return board, size

def divide_triangle(end1, end2, end3, randomness):  # oblicza srodki dostaje trojkat i zwraca srodkowy 3 a fajnie by bylo gdyby zwracal 4 trojkaty
    mid1,mid2,mid3 = [0,0,0],[0,0,0],[0,0,0]
    #print(f"end = {end1[0] + end2[0]}")
    mid1[0] = (end1[0] + end2[0])//2 #x
    mid1[1]= (end1[1] + end2[1])//2 #Y
    mid1[2] = ((end1[2] + end2[2])//2) +random.randint(-randomness, randomness) #value

    mid2[0] = (end2[0] + end3[0])//2
    mid2[1] = (end2[1] + end3[1])//2
    mid2[2] = ((end2[2] + end3[2]) // 2) + random.randint(-randomness, randomness)

    mid3[0] = (end1[0] + end3[0])//2
    mid3[1] = (end1[1] + end3[1])//2
    mid3[2] = ((end1[2] + end3[2]) // 2) + random.randint(-randomness, randomness)

    t1 = [end1, mid1, mid3]
    t2 = [mid1, end2, mid2]
    t3 = [mid1, mid3, mid2]
    t4 = [mid3, mid2, end3]
    #print(f'mid1 = {mid1}')
    return [t1,t2,t3,t4]

def split_triangles(triangles, randomness, board):
    new_triangles = []
    for triangle in triangles:
        # print(triangle)
        temp = divide_triangle(triangle[0], triangle[1], triangle[2], randomness)
        new_triangles.append(temp[0])
        new_triangles.append(temp[1])
        new_triangles.append(temp[2])
        new_triangles.append(temp[3])
    triangles = new_triangles
    for triangle in triangles:
        for point in triangle:
            if board[point[0]][point[1]] == 1:
                board[point[0]][point[1]] = point[2]
            else:
                point[2] = board[point[0]][point[1]]
    return triangles, board

def triangle_board(lvl):
    #board, size = generate_board(lvl)
    board,size = generate_board_squ(lvl)
    randomness = 2**lvl-1
    board[0][0] = random.randint(-randomness, randomness)
    board[size][0] = random.randint(-randomness, randomness)
    board[size][size] = random.randint(-randomness, randomness)
    board[0][size] = random.randint(-randomness, randomness)

    tile_size = size
    triangles_v1 = [[[0,0, board[0][0]], [size, 0, board[size][0]], [size, size, board[size][size]]]]
    triangles_v2 = [[[0,0, board[0][0]], [size, size, board[size][size]], [0,size, board[0][size]]]]
    for i in range(lvl):
        triangles_v1, board = split_triangles(triangles_v1, randomness, board)
        triangles_v2, board = split_triangles(triangles_v2, randomness, board)
        randomness = max(randomness // 2, 1)
    # for triangle in triangles:
    #     for point in triangle:
    #         #print(point)
    #         board[point[0]][point[1]] = point[2]

    return  board
#def smooth(board, windows_size):


board = triangle_board(7)
surf = mlab.surf(board, colormap='gist_earth', warp_scale='auto')
#mlab.show()
mlab.imshow(board, colormap='gist_earth')
mlab.show()

#wygladzanie
#2 trojkat