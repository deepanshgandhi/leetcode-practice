class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        adj_list = {}
        adj_list[beginWord] = []
        word_len = len(beginWord)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(word_len):
                pattern = word[:i]+"*"+word[(i+1):]
                if pattern not in adj_list:
                    adj_list[pattern] = []
                adj_list[pattern].append(word)
        visited = set([beginWord])
        q = deque([beginWord])
        ans = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                neighbors = []
                for i in range(word_len):
                    pattern = word[:i]+"*"+word[(i+1):]
                    neighbors.extend(adj_list[pattern])
                for neighbor in neighbors:
                    if neighbor == endWord:
                        return ans+1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        q.append(neighbor)
            ans+=1
        return 0
