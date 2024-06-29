class Solution:
    def dfs(self, graph, parent, curr, ans, visited):
        visited[curr] = True
        for i in graph[curr]:
            if not visited[i]:
                ans[i].append(parent)
                self.dfs(graph,parent,i,ans,visited)

    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        ans = [[] for _ in range(n)]
        graph = [[] for _ in range(n)]

        for i in edges:
            graph[i[0]].append(i[1])

        for i in range(n):
            self.dfs(graph,i,i,ans, [False]*n)

        return ans 