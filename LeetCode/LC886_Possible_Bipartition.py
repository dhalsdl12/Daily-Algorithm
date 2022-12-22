class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)

        for a, b in dislikes:
            graph[a ].append(b)
            graph[b ].append(a)
        
        color = [0 for _ in range(n + 1)]

        for i in range(1, n + 1):
            if color[i] != 0:
                continue
            tmp = collections.deque()
            tmp.append(i)
            color[i] = 1

            while tmp:
                cur = tmp.popleft()
                for e in graph[cur]:
                    if color[e] != 0:
                        if color[cur] == color[e]:
                            return False
                    else:
                        color[e] = -color[cur]
                        tmp.append(e)

        return True