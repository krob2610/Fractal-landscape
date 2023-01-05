import numpy as np
import random
from mayavi import mlab
from itertools import chain
from helpers import smooth
from pprint import pprint

import math
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

def divide_triangle(end1, end2, end3, randomness, biom):  # oblicza srodki dostaje trojkat i zwraca srodkowy 3 a fajnie by bylo gdyby zwracal 4 trojkaty

    if biom == "water":
        mid1, mid2, mid3 = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        # print(f"end = {end1[0] + end2[0]}")
        mid1[0] = (end1[0] + end2[0]) // 2  # x
        mid1[1] = (end1[1] + end2[1]) // 2  # Y
        mid1[2] = ((end1[2] + end2[2]) // 2) + random.randint(-randomness*3, int(randomness/6))  # value

        mid2[0] = (end2[0] + end3[0]) // 2
        mid2[1] = (end2[1] + end3[1]) // 2
        mid2[2] = ((end2[2] + end3[2]) // 2) + random.randint(-randomness*3, int(randomness/6))

        mid3[0] = (end1[0] + end3[0]) // 2
        mid3[1] = (end1[1] + end3[1]) // 2
        mid3[2] = ((end1[2] + end3[2]) // 2) + random.randint(-randomness*3, int(randomness/6))
    else:
        mid1, mid2, mid3 = [0, 0, 0], [0, 0, 0], [0, 0, 0]
        # print(f"end = {end1[0] + end2[0]}")
        mid1[0] = (end1[0] + end2[0]) // 2  # x
        mid1[1] = (end1[1] + end2[1]) // 2  # Y
        mid1[2] = ((end1[2] + end2[2]) // 2) + random.randint(-randomness, randomness)  # value

        mid2[0] = (end2[0] + end3[0]) // 2
        mid2[1] = (end2[1] + end3[1]) // 2
        mid2[2] = ((end2[2] + end3[2]) // 2) + random.randint(-randomness, randomness)

        mid3[0] = (end1[0] + end3[0]) // 2
        mid3[1] = (end1[1] + end3[1]) // 2
        mid3[2] = ((end1[2] + end3[2]) // 2) + random.randint(-randomness, randomness)
    t1 = [end1, mid1, mid3]
    t2 = [mid1, end2, mid2]
    t3 = [mid1, mid3, mid2]
    t4 = [mid3, mid2, end3]
    #print(f'mid1 = {mid1}')
    return [t1,t2,t3,t4]

def split_triangles(triangles, randomness, board, biom):
    new_triangles = []
    for triangle in triangles:
        # print(triangle)
        temp = divide_triangle(triangle[0], triangle[1], triangle[2], randomness, biom)
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
def combine_boards(boards):
    end_matrix = None

    counter = 0
    for i in range(int(math.sqrt(len(boards)))):
        new_b = boards[counter].copy()
        for j in range(1, int(math.sqrt(len(boards)))):
            #print(counter)
            new_b = np.hstack((np.array(new_b), np.array(boards[counter+1]))).tolist()
            counter += 1
        counter+=1
        if end_matrix == None:
            end_matrix = new_b.copy()
        else:
            end_matrix =end_matrix + new_b
    return end_matrix
def triangle_board(lvl, multiplier = None, negative_only = False, positive_only = False, biom = None):
    #board, size = generate_board(lvl)
    board,size = generate_board_squ(lvl)
    randomness = 2**lvl-1

    board[0][0] = random.randint(-randomness, randomness)
    board[size][0] = random.randint(-randomness, randomness)
    board[size][size] = random.randint(-randomness, randomness)
    board[0][size] = random.randint(-randomness, randomness)
    if biom == "water":
        board[0][0] = random.randint(-randomness, 0)
        board[size][0] = random.randint(-randomness, 0)
        board[size][size] = random.randint(-randomness, 0)
        board[0][size] = random.randint(-randomness, 0)
    tile_size = size
    triangles_v1 = [[[0,0, board[0][0]], [size, 0, board[size][0]], [size, size, board[size][size]]]]
    triangles_v2 = [[[0,0, board[0][0]], [size, size, board[size][size]], [0,size, board[0][size]]]]
    for i in range(lvl):
        triangles_v1, board = split_triangles(triangles_v1, randomness, board, biom)
        triangles_v2, board = split_triangles(triangles_v2, randomness, board, biom)
        randomness = max(randomness // 2, 1)
    # for triangle in triangles:
    #     for point in triangle:
    #         #print(point)
    #         board[point[0]][point[1]] = point[2]
    # if multiplier:
    #     board = [[el+(2**lvl-1) for el in row] for row in board]
    if negative_only:
        #print("uwu")
        return [[el if el < 0 else el * -1 for el in row] for row in board]

    if positive_only:
        #print("uwu")
        return [[el if el > 0 else el * -1 for el in row] for row in board]

    return board
#def smooth(board, windows_size):


# board = triangle_board(7)
# surf = mlab.surf(board, colormap='gist_earth', warp_scale='auto')
#
# #mlab.show()
# mlab.imshow(board, colormap='gist_earth')
# mlab.show()
def preaty_print(tab):
    for row in tab:
        print(row)
def create_empty(size):
    return [[0]*size for s in range(size)]
def create_water(size, m):
    return [[m]*size for s in range(size)]
#
# water_board = triangle_board(6,multiplier= True , negative_only = True, )
# water_board_v2 = triangle_board(6, multiplier = True, negative_only = True)

n_board = triangle_board(6, positive_only=True)
n_board_v2 = triangle_board(6, positive_only=True)
n_board_v3 = triangle_board(6,positive_only=True)

lake_board = triangle_board(6, negative_only=True)
lake_board_v2 = triangle_board(6, negative_only=True)
lake_board_v3 = triangle_board(6,negative_only=True)


empty_1 = create_empty(len(n_board))
empty_2 = create_empty(len(n_board))
empty_3 = create_empty(len(n_board))

board = combine_boards([empty_1,empty_2,empty_3,lake_board,lake_board_v2,lake_board_v3,n_board,n_board_v2,n_board_v3])

def min_water(b):
    t = sum(b, [])
    return min(t)
m = min_water(board)
w_board_1 = create_water(len(n_board), m+10)
w_board_2 = create_water(len(n_board), m+10)
w_board_3 = create_water(len(n_board), m+10)
print(m)
board = combine_boards([w_board_1,w_board_2,w_board_3,lake_board,lake_board_v2,lake_board_v3,n_board,n_board_v2,n_board_v3])

def scale_up(b, f):
    t = sum(b, [])
    minimal =  min(t)
    print(minimal/f)
    for i in range(len(b)):
        for j in range(len(b)):
            if b[i][j]<=minimal/f:
                b[i][j] = b[i][j]/f
    return b
#board = scale_up(board,2)

surf = mlab.surf(board, colormap='gist_earth', warp_scale='auto', )

#mlab.show()
mlab.imshow(board, colormap='gist_earth')
mlab.show()

# l1 = [[1,2],
#       [3,4]]
#
#
# l2 = [[0,0],
#       [0,0]]
#
# # print(l1+l2) #to dol
# l3 = np.hstack((np.array(l1), np.array(l2))).tolist()
# print(np.hstack((np.array(l3), np.array(l2))).tolist())
# surf = mlab.surf(board, colormap='gist_earth', warp_scale='auto')
#
#
# mlab.imshow(board, colormap='gist_earth')
# mlab.show()

#wygladzanie
#2 trojkat