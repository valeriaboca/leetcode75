from typing import List

# 724. Find Pivot Index
def pivotIndex(nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sum, right_sum = 0, 0
        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]
            if left_sum == right_sum:
                return i
            left_sum += nums[i]
        return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))