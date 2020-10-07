class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        grid = [[1] * N for i in range(N)]

        down = [[0] * N for i in range(N)]
        right = [[0] * N for i in range(N)]
        up = [[0] * N for i in range(N)]
        left = [[0] * N for i in range(N)]

        for mine in mines:
            grid[mine[0]][mine[1]] = 0

        # down
        for i in range(N):
            for j in range(N):
                addOn = 0
                if i != 0:
                    addOn = down[N - i][j]
                if grid[N - i - 1][j] != 0:
                    down[N - i - 1][j] = grid[N - i - 1][j] + addOn
                else:
                    down[N - i - 1][j] = 0
        # print(down)

        # right
        for i in range(N):
            for j in range(N):
                addOn = 0
                if j != 0:
                    addOn = right[i][N - j]

                if grid[i][N - j - 1] != 0:
                    right[i][N - j - 1] = grid[i][N - j - 1] + addOn
                else:
                    right[i][N - j - 1] = 0
        # print(right)

        # up
        for i in range(N):
            for j in range(N):
                addOn = 0
                if i != 0:
                    addOn = up[i - 1][j]
                if grid[i][j] != 0:
                    up[i][j] = grid[i][j] + addOn
                else:
                    up[i][j] = 0
        # print(up)

        # left
        for i in range(N):
            for j in range(N):
                addOn = 0
                if j != 0:
                    addOn = left[i][j - 1]

                if grid[i][j] != 0:
                    left[i][j] = grid[i][j] + addOn
                else:
                    left[i][j] = 0
        # print(left)

        maxSeen = 0
        for r in range(N):
            for c in range(N):
                v = min(up[r][c], down[r][c], left[r][c], right[r][c])
                maxSeen = max(maxSeen, v)

        print(maxSeen)
        return maxSeen
