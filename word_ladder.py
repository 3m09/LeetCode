def ladderLength(beginWord: str, endWord: str, wordList) -> int:
        from collections import deque
        dist = [-1 for _ in wordList]
        root_adjacencies = deque()
        dest = -1
        word_len = len(beginWord)
        for i,word in enumerate(wordList):
            mismatch_cnt = 0
            isEndWord = True
            for l in range(word_len):
                if(word[l] != endWord[l]):
                    isEndWord = False
                    break
            dest = i if isEndWord else -1
            for c_idx in range(word_len):
                if word[c_idx] != beginWord[c_idx]:
                    mismatch_cnt += 1
            if mismatch_cnt == 1:
                root_adjacencies.append(i)
                dist[i] = 1
                if dest == i:
                    return 2
        if dest == -1:
            return 0
        while root_adjacencies:
            node = root_adjacencies.popleft()
            for j in range(len(wordList)):
                if dist[j] != -1:
                    continue
                mismatch_cnt = 0
                for c_idx in range(word_len):
                    if wordList[node][c_idx] != wordList[j][c_idx]:
                        mismatch_cnt += 1
                if mismatch_cnt == 1:
                    dist[j] = dist[node] + 1
                    root_adjacencies.append(j)
                    if j == dest:
                        return dist[j] + 1
        return 0
                    
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    print(ladderLength(beginWord, endWord, wordList))