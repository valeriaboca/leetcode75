from typing import Counter

# 1657 Determine if Two Strings Are Close
def closeStrings(word1: str, word2: str) -> bool:
        set1 = set(word1)
        set2 = set(word2)

        count1 = Counter(word1)
        count2 = Counter(word2)
        
        if sorted(count1.values()) == sorted(count2.values()) and set1 == set2:
            return True
        return False

word1 = "cabbba"
word2 = "abbccc"

print(closeStrings(word1, word2))

# Hash Table, String, Sorting, Counting