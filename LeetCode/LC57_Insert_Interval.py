class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        start, end = newInterval
        for a, b in intervals:
            if b < start:
                answer.append([a, b])
            elif a > end:
                answer.append([start, end])
                start, end = a, b
            elif b >= start or a <= end:
                start = min(start, a)
                end = max(end, b)
                
        answer.append([start, end]) 
        return answer