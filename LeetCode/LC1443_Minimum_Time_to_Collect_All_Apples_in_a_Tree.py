class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            time = 0
            apple = hasApple[node]
            visit[node] = 1

            for n in edge[node]:
                if visit[n] == 0:
                    subapple, subtime = dfs(n)
                    apple = apple or subapple

                    if subapple:
                        time += subtime + 2
            return apple, time

        edge = defaultdict(list)
        visit = [0 for _ in range(n)]
        for a, b in edges:
            edge[a].append(b)
            edge[b].append(a)

        return dfs(0)[1]