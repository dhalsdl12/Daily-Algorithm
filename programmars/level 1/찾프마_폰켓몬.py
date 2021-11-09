def solution(nums):
    answer = 0
    type_p = set(nums)
    num = len(nums)
    
    if num/2 >= len(type_p):
        return len(type_p)
    else:
        return num/2
