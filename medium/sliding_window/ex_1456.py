
# 1456. Maximum Number of Vowels in a Substring of Given Length
def maxVowels(s: str, k: int) -> int:
    vowels = 'aeiou'

    vowel_count = 0
    for i in range(k):
        if s[i] in vowels:
            vowel_count += 1
        
    max_vowel_count = vowel_count
    for j in range(k, len(s)):
        if s[j - k] in vowels:
            vowel_count -= 1
        if s[j] in vowels:
            vowel_count += 1
        max_vowel_count = max(max_vowel_count, vowel_count)
    return max_vowel_count

s = "abciiidef"
k = 3
print(maxVowels(s, k))