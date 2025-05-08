from typing import List

# 605. Can Place Flowers
def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
        for i in range(len(flowerbed)):
            prev = flowerbed[i - 1] if i > 0 else 0
            next = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0

            if flowerbed[i] == 0 and prev == 0 and next == 0:
                flowerbed[i] = 1
                n -= 1
                
                if n == 0:
                    return True
        return n <= 0

flowerbed = [1,0,0,0,1]
n = 1
print(canPlaceFlowers(flowerbed, n))