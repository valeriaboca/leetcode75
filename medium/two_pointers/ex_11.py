from typing import List

# 11. Container With Most Water
def maxArea(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_area = 0

    while left < right:
        area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, area)
            
        if left >= right:
            right -= 1
        else:
            left += 1
                
    return max_area

# Brute Force
#def maxArea(height: List[int]) -> int:
#        max_area = 0
#        for i in range(len(height)):
#            for j in range(i + 1, len(height)):
#                area = min(height[i], height[j]) * (j - i)
#                max_area = max(max_area, area)
#        return max_area
#

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))