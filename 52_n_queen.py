class Solution:
    def totalNQueens(self, n: int) -> int:
        def placeQueen(col,diag,xdiagon,r,c):
            nonlocal n
            d = (n-1) - c + r
            xd = r + c
            if not col[c] and not diag[d] and not xdiagon[xd]:
                col[c] = True
                diag[d] = True
                xdiagon[xd] = True
                return True
            return False
        
        def removeQueen(col,diag,xdiagon,r,c):
            nonlocal n
            d = (n-1) - c + r
            xd = r + c
            if col[c] and diag[d] and xdiagon[xd]:
                col[c] = False
                diag[d] = False
                xdiagon[xd] = False
                return True
            return False
        
        def solve(col,diag,xdiagon,r):
            nonlocal n
            if r == n:
                return 1
            num_sol = 0
            for i in range(n):
                can_add = placeQueen(col,diag,xdiagon,r,i)
                if not can_add:
                    continue
                num_sol += solve(col,diag,xdiagon,r+1)
                removeQueen(col,diag,xdiagon,r,i)
            return num_sol
        if n == 2 or n == 3:
            return 0
        col = [False] * n
        diag = [False] * (2*n - 1)
        xdiag = [False] * (2*n - 1)
        return solve(col,diag,xdiag,0)
        
