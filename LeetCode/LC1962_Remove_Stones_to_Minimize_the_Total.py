class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        result = sum(piles)
        pile = [-piles[i] for i in range(len(piles))]
        heapq.heapify(pile)
        
        for _ in range(k):
            p = heapq.heappop(pile)
            result -= (-p) // 2
            heapq.heappush(pile, p + (-p) // 2)
            
        return result