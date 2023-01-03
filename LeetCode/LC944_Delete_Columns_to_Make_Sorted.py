class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        answer = 0
        for j in range(len(strs[0])):
            tmp = []
            for i in range(len(strs)):
                tmp.append(strs[i][j])
            
            tmp2 = sorted(tmp)
            if tmp != tmp2:
                answer += 1
        
        return answer