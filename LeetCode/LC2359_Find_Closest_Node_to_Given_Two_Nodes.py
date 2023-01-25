import heapq

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        def dijkstra(x):
            dist = [-1 for _ in range(len(edges))]
            dist[x] = 0
            heap=[(0, x)]

            while heap:
                d, node = heapq.heappop(heap)
                if d != dist[node]:
                    continue
                if edges[node] != -1:
                    nei = edges[node]
                    cur = d + 1
                    if dist[nei] == -1 or cur < dist[nei]:
                        dist[nei] = cur
                        heapq.heappush(heap, (cur, nei))
            return dist

        d1 = dijkstra(node1)
        d2 = dijkstra(node2)
        answer = -1
        val = 999999999

        for i in range(len(edges)):
            if d1[i] >= 0 and d2[i] >= 0:
                cur = max(d1[i], d2[i])
                if cur < val:
                    val = cur
                    answer = i
                    
        return answer