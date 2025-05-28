from typing import List

# 1493. Longest Subarray of 1's After Deleting One ELement 
def longestSubarray(nums: List[int]) -> int:
        left,zero_count = 0, 0
        max_len = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            length = (right - left)
            max_len = max(max_len, length)
        return max_len

nums = [0,1,1,1,0,1,1,0,1]
print(longestSubarray(nums))

# Array, Dynamic Programming, Sliding Window