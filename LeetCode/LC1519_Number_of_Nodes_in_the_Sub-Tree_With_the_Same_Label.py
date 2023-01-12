class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        def dfs(node):
            nonlocal visit, tree, answer
            cnt = collections.Counter(labels[node])
            visit[node] = 1
            for nn in tree[node]:
                if visit[nn] == 0:
                    visit[nn] = 1
                    cnt += dfs(nn)
            answer[node] += cnt.get(labels[node])
            return cnt

        answer = [0 for _ in range(n)]
        visit = [0 for _ in range(n)]
        tree = defaultdict(list)
        for a, b in edges:
            tree[a].append(b)
            tree[b].append(a)
        
        dfs(0)

        return answer