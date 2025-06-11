from typing import List

# 1207. Unique Number of Occurrences
def uniqueOccurrences(arr: List[int]) -> bool:
        hashmap = {}
        for i in arr:
            if i in hashmap:
                hashmap[i] += 1
            else:
                hashmap[i] = 1
                
        unique_count = set(hashmap.values())
        if len(hashmap) == len(unique_count):
            return True
        return False

arr = [1,2,2,1,1,3]
print(uniqueOccurrences(arr))

# Array, Hash Table