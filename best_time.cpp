class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        s1 = -prices[0]
        s2 = float('-inf') 
        s3 = float('-inf') 
        s4 = float('-inf') 
        for price in prices:
            s1 = max(s1,-price)
            s2 = max(s2, s1 + price)
            s3 = max(s3, s2 - price)
            s4 = max(s4, s3 + price)
        return max( s4, 0 )