class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        check = [capacity[i] - rocks[i] for i in range(len(rocks))]
        check.sort()
        s = 0
        cnt = 0
        for c in check:
            s += c
            if s <= additionalRocks:
                cnt += 1
            else:
                break
        return cnt