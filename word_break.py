class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        candidates = [""]
        dp = [False] * (len(s) + 1)
        dp[-1] = True
        for i in range(len(s)-1,-1,-1):
            tmp = s[i]
            for j in range(len(candidates)-1,-1,-1):
                tmp += candidates[j]
                if tmp in wordDict:
                    dp[i] = True
                    break
            candidates[-1] = s[i] + candidates[-1]
            if dp[i]:
                candidates.append("")
        return dp[0]
