from typing import List

# 2215. Find the Difference of Two Arrays
def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hs1, hs2 = set(nums1), set(nums2)
        list1 = list(hs1.difference(hs2))
        list2 = list(hs2.difference(hs1))
        return [list1, list2]

nums1 = [1,2,3]
nums2 = [2,4,6]
print(findDifference(nums1, nums2))

# Array, Hash Table