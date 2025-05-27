from typing import List

# 1004. Max Consecutive Ones III
def longestOnes(nums: List[int], k: int) -> int:
        left, zero_count, max_len = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len

nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
print(longestOnes(nums, k))

# Arrays, Sliding Window