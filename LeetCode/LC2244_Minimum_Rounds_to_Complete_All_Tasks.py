from collections import Counter

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0
        cnt = Counter(tasks)
        nums = cnt.values()
        
        if 1 in nums:
            return -1
        
        for num in nums:
            if num % 3 == 0:
                answer += num // 3
            elif num % 3 == 1:
                answer += num // 3 + 1
            else:
                answer += num // 3 + 1

        return answer