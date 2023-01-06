class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer = 0
        costs.sort()

        for c in costs:
            if c <= coins:
                answer += 1
                coins -= c
            else:
                break
        
        return answer