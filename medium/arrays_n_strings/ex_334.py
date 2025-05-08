from math import inf
from typing import List

# 334. Increasing Triplet Subsequence
def increasingTriplet(nums: List[int]) -> bool:
        first = inf
        second = inf
        for i in range(len(nums)):
            if nums[i] <= first:
                first = nums[i]
            elif nums[i] <= second:
                second = nums[i]
            else:
                return True
        return False

nums = [2,1,5,0,4,6]
print(increasingTriplet(nums))