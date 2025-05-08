from typing import List

# 238. Product of Array Except Self
def productExceptSelf(nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] *= prefix
            prefix *= nums[i]
            # return answer
            
        suffix = 1
        for j in range(len(nums) - 1, -1, -1):
            answer[j] *= suffix
            suffix *= nums[j]
        return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))