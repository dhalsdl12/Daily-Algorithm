class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        result = []
        for q in queries:
            s = 0
            c = 0
            check = 0
            for i in range(len(nums)):
                s += nums[i]
                if s > q:
                    result.append(c)
                    check = 1
                    break
                else:
                    c += 1
            if check == 0:
                result.append(len(nums))
        return result
