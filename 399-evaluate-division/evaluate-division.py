class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj_list = {}
        for i, eq in enumerate(equations):
            src,dst = eq
            wt = values[i]
            if src not in adj_list:
                adj_list[src]=[]
            if dst not in adj_list:
                adj_list[dst]=[]
            adj_list[src].append([dst,wt])
            adj_list[dst].append([src,1/wt])
        def bfs(src,dst):
            if src not in adj_list or dst not in adj_list:
                return -1
            q=deque()
            visit = set()
            q.append((src,1))
            visit.add(src)
            while q:
                node,w = q.popleft()
                if node==dst:
                    return w
                for n in adj_list[node]:
                    neighbor,wt=n
                    if neighbor not in visit:
                        q.append((neighbor,w*wt))
                        visit.add(neighbor)
            return -1
            
        res = []
        return [bfs(q[0],q[1]) for q in queries]