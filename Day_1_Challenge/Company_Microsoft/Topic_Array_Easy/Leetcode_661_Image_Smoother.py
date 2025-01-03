# Leetcode Solution [For thought process and approach, Do read the readme file of this folder!] 
import math
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        m,n = len(img), len(img[0])
        result = [[0]*n for _ in range(m)]

        # Valid neighbor positions. 
        valid_directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]

        # loop
        for i in range(m):
            for j in range(n):
                # total and count for average.
                total = 0
                count = 0

                # check for neighbor cells.
                for di, dj in valid_directions:
                    pos_i, pos_j = i + di, j + dj

                    # check is this valid.
                    if (0 <= pos_i < m) and (0 <= pos_j < n):
                        total += img[pos_i][pos_j]
                        count += 1
                # current cell iself.
                total += img[i][j]
                count += 1

                # Result of the cell.
                result[i][j] = math.floor(total/count) 
        return result
