class Trie:

    def __init__(self):
        self.data = [[{'children':{},'isEnd':False}]]

    def insert(self, word: str) -> None:
        node = 0
        level = 0
        start_from = -1
        for i,c in enumerate(word):
            if c in self.data[level][node]['children']:
                node = self.data[level][node]['children'][c]
                level += 1
            else:
                start_from = i
                break
        if start_from == -1:
            self.data[level][node]['isEnd'] = True
            return
        for i in range(start_from,len(word)):
            if level == len(self.data) - 1:
                self.data.append([])
            nw_node = len(self.data[level+1])
            self.data[level][node]['children'][word[i]] = nw_node
            self.data[level+1].append({'children':{},'isEnd':False})
            level = level+1
            node = nw_node
        self.data[level][node]['isEnd'] = True

    def search(self, word: str) -> bool:
        node = 0
        level = 0
        contains = True
        for i,c in enumerate(word):
            if c in self.data[level][node]['children']:
                node = self.data[level][node]['children'][c]
                level += 1
            else:
                contains = False
                break
        return True if contains and self.data[level][node]['isEnd'] else False

    def startsWith(self, prefix: str) -> bool:
        node = 0
        level = 0
        contains = True
        for i,c in enumerate(prefix):
            if c in self.data[level][node]['children']:
                node = self.data[level][node]['children'][c]
                level += 1
            else:
                contains = False
                break
        return contains
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)