from typing import Counter, List

# 1679. Max Number of K-Sum Pairs
def maxOperations(nums: List[int], k: int) -> int:
        counter = Counter(nums)
        result = 0

        for num in list(counter):
            complement = k - num
            if counter[num] > 0 and counter[complement] > 0:
                if num == complement:
                    count = counter[num] // 2
                    result += count
                    counter[num] -= count * 2
                else:
                    min_count = min(counter[num], counter[complement])
                    result += min_count
                    counter[num] -= min_count
                    counter[complement] -= min_count
        return result

nums = [1,2,3,4]
k = 5
print(maxOperations(nums, k))