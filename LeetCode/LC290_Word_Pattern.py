class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split(' ')
        if len(pattern) != len(arr):
            return False
        pdic = {}
        sdic = {}
        for i in range(len(pattern)):
            p = pattern[i]
            a = arr[i]
            if (p in pdic and pdic[p] != a) or (a in sdic and sdic[a] != p):
                return False
            pdic[p] = a
            sdic[a] = p

        return True
