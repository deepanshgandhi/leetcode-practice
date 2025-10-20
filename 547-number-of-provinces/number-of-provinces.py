class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        n = len(isConnected)
        provinces = 0
        def dfs(index):
            self.visited.add(index)
            for j in range(n):
                if isConnected[index][j] and j not in self.visited:
                    dfs(j)
            return 
        for i in range(n):
            if i not in self.visited:
                provinces+=1
                dfs(i)
        return provinces