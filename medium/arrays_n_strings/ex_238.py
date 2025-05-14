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


# Brute Force Solution
# def productExceptSelf(nums: List[int]) -> List[int]:
        
#     prefix = [nums[0]]
#     for i in range(1, len(nums)):
#         prefix.append(nums[i] * prefix[i -1])        

#     suffix = [1] * len(nums)
#     suffix[len(nums) - 1] = nums[-1]
#     for j in range(len(nums) -2, -1, -1):
#         suffix[j] = nums[j] * suffix[j + 1]

#     answer = []
#     for i in range(len(nums)):
#         if i == 0:
#             answer.append(suffix[i + 1])
#         elif i == len(nums) - 1:
#                 answer.append(prefix[i - 1])
#         else:
#             answer.append(prefix[i - 1] * suffix[i + 1])
#     return answer

nums = [1,2,3,4]
print(productExceptSelf(nums))