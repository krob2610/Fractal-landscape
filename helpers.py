import numpy as np

def smooth(board, blockSize, maxDev):
    newBoard = board
    for i in range(len(newBoard) - (blockSize - 1)):
        for j in range(len(newBoard) - (blockSize - 1)):
            block = newBoard[i:i+blockSize, j:j+blockSize]
            mean = block.mean()
            biggerDif = np.where(abs(block) > (abs(mean) + maxDev))
            rowIdx = biggerDif[0]
            colIdx = biggerDif[1]
            if len(rowIdx) > 0:
                for i in range(len(rowIdx)):
                    if mean >= 0:
                        block[rowIdx[i]][colIdx[i]] = mean + maxDev
                    else:
                        block[rowIdx[i]][colIdx[i]] = mean - maxDev
                newBoard[i:i+blockSize, j:j+blockSize] = block
    return newBoard