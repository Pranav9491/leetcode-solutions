class Solution:
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        graph = [[] for i in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited=[False]*n
        q=[]
        q.append(source)
        visited[source] = True
        while len(q)> 0:
            a=q.pop()
            if a==destination:
                return True
            for neighbour in graph[a]:
                if visited[neighbour]==False:
                    q.append(neighbour)
                    visited[neighbour]=True
        return False