from typing import List

# 643. Maximum Average Subarray I
def findMaxAverage(nums: List[int], k: int) -> float:
        max_seen = sum(nums[0:k])
        current_window = max_seen
        for i in range(1,(len(nums) - k) + 1):
            current_window -= nums[i -1]
            current_window += nums[i+k-1]
            max_seen = max(max_seen, current_window)
        return max_seen / k

nums = [1,12,-5,-6,50,3]
k = 4
print(findMaxAverage(nums, k))