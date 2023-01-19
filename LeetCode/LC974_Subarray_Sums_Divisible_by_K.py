class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] =1
        output = 0
        Sum = 0
        for n in nums:
            Sum +=n
            m = Sum%k
            output += dic[m]
            dic[m]+=1
        
        return output