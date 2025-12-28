class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r = len(matrix)
        c = len(matrix[0]) if r > 0 else 0
        dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
        mx = 0
        for i in range(r-1,-1,-1):
            for j in range(c-1,-1,-1):
                if int(matrix[i][j]) == 1 and dp[i][j] == 0:
                    dp[i][j] = min(dp[i][j+1],dp[i+1][j],dp[i+1][j+1]) + 1
                    mx = max(dp[i][j],mx)
        return mx * mx

        