class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        for i in range(2, len(nums) + 1):
            for x in set(itertools.combinations(nums,i)):
                check = 0
                for a, b in zip(x, x[1:]):
                    if a <= b:
                        continue
                    else:
                        check = 1
                if check == 0:
                    answer.append(x)


        return answer
