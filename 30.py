from typing import List
from collections import Counter

# ...existing code...
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        wl = len(words[0])
        n = len(s)
        m = len(words)
        word_counts = Counter(words)
        ans: List[int] = []

        for i in range(wl):
            left = i
            tmp_counts = {}
            count = 0
            for j in range(i, n - wl + 1, wl):
                w = s[j:j+wl]
                if w in word_counts:
                    tmp_counts[w] = tmp_counts.get(w, 0) + 1
                    count += 1
                    # shrink window until counts are valid
                    while tmp_counts[w] > word_counts[w]:
                        left_w = s[left:left+wl]
                        tmp_counts[left_w] -= 1
                        left += wl
                        count -= 1
                    if count == m:
                        ans.append(left)
                        # move left by one word to look for next match
                        left_w = s[left:left+wl]
                        tmp_counts[left_w] -= 1
                        left += wl
                        count -= 1
                else:
                    tmp_counts.clear()
                    count = 0
                    left = j + wl
        return ans
