from typing import List

# 1732. Find the Highest Altitude
def largestAltitude(gain: List[int]) -> int:
        p = [0] * (len(gain) + 1)
        for i in range(len(gain)):
            p[i+1] = p[i] + gain[i]
        return max(p)

gain = [-5,1,5,0,-7]
print(largestAltitude(gain))

# Array, Prefix Sum