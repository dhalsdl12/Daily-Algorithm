class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            else:
                return gcd(y, x % y)
    

        if len(points) == 1:
            return 1

        answer = 0
        for i in range(len(points)):
            dic = defaultdict(int)

            for j in range(i + 1, len(points)):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx == 0:
                    dic[(0, points[i][1])] += 1
                elif dy == 0:
                    dic[(points[i][0], 0)] += 1
                else:
                    d = gcd(dx, dy)
                    dic[(dx//d, dy//d)] += 1

            for v in dic.values():
                answer = max(answer, v)

        return answer + 1