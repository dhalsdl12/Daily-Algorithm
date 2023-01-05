class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        answer = 1
        points.sort(key = lambda x:x[1])
        shot = points[0][1]

        for i in range(1, len(points)):
            if points[i][0] <= shot:
                continue
            else:
                shot = points[i][1]
                answer += 1
        
        return answer