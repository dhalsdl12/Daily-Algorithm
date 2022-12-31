class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        def dfs(node, path):
            if node == n - 1:
                answer.append(path[:]) 
            for n_node in graph[node]:
                path.append(n_node)
                dfs(n_node, path)
                path.remove(n_node)

        
        answer = []
        n = len(graph)

        dfs(0, [0])
        return answer