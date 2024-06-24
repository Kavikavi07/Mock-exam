def uniquePathsWithObstacles(grid):
    if not grid or not grid[0]:
        return 0
    
    m, n = len(grid), len(grid[0])
    
    dp = [[0] * n for _ in range(m)]
    
    if grid[0][0] == 0:
        dp[0][0] = 1
    else:
        dp[0][0] = 0
    
    for j in range(1, n):
        if grid[0][j] == 0:
            dp[0][j] = dp[0][j-1]
        else:
            dp[0][j] = 0
    
    for i in range(1, m):
        if grid[i][0] == 0:
            dp[i][0] = dp[i-1][0]
        else:
            dp[i][0] = 0
    
    
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
            else:
                dp[i][j] = 0
    
    return dp[m-1][n-1]


grid = [
    [0,0,0],
    [0,1,0],
    [0,0,0]
]
print(uniquePathsWithObstacles(grid))