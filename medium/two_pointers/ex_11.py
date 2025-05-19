from typing import List

# 11. Container With Most Water



# Brute Force
def maxArea(height: List[int]) -> int:
        max_area = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                area = min(height[i], height[j]) * (j - i)
                max_area = max(max_area, area)
        return max_area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))