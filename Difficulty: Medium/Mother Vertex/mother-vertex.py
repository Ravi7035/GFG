class Solution:
    def findMotherVertex(self, V, edges):
        from collections import defaultdict

        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)

        visited = [False] * V
        candidate = 0

        # Step 1: Find last finished vertex
        def dfs(node):
            visited[node] = True
            for nei in graph[node]:
                if not visited[nei]:
                    dfs(nei)

        for i in range(V):
            if not visited[i]:
                dfs(i)
                candidate = i

        # Step 2: Verify candidate
        visited = [False] * V
        dfs(candidate)

        if all(visited):
            return candidate
        return -1