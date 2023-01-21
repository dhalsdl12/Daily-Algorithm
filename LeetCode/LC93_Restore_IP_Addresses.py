class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        def dfs(idx, cnt):
            if cnt == 0:
                if idx == len(s):
                    answer.append('.'.join(tmp[:]))
                    return
                return
            
            for i in range(idx, min(idx + 3, len(s))):
                t = s[idx:i + 1]
                if (cnt * 3 < len(s[i:]) or (t[0] == "0" and len(t) > 1) or int(t) > 255):
                    return
                
                tmp.append(t)
                dfs(i + 1, cnt - 1)
                tmp.pop()


        answer = []
        tmp = []

        if len(s) < 4 or len(s) > 12:
            return answer
        
        dfs(0, 4)
        return answer
