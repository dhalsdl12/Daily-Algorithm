class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        zero = s.count('0')
        one = 0
        answer = zero + one
        for i in range(len(s)):
            if s[i] == '0':
                zero -= 1
            else:
                one += 1
            answer = min(answer, zero + one)
        
        return answer