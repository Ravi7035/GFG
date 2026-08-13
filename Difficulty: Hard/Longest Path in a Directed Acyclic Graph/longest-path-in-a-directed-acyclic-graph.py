class Solution:
    def maxDistance(self, V, src, edges):
        
        graph = [[] for _ in range(V)]

        for u, v, w in edges:
            graph[u].append((v, w))

        visited = [False] * V
        topo = []

        def dfs(u):
            visited[u] = True

            for v, w in graph[u]:
                if not visited[v]:
                    dfs(v)

            topo.append(u)

        for i in range(V):
            if not visited[i]:
                dfs(i)

        topo.reverse()

        dist = [-2**31] * V
        dist[src] = 0

        for u in topo:
            if dist[u] == -2**31:
                continue

            for v, w in graph[u]:
                dist[v] = max(dist[v], dist[u] + w)

        return dist