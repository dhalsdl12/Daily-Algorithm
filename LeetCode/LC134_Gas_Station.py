class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        i = 0

        while i < len(gas):
            gass = 0
            costs = 0
            cnt = 0

            while cnt < len(gas):
                idx = (i + cnt) % len(gas)
                gass += gas[idx]
                costs += cost[idx]
                if gass < costs:
                    break
                cnt += 1
            
            if cnt == len(gas):
                return i
            else:
                i = i + cnt + 1
        
        return -1