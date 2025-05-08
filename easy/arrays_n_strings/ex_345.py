
# 345. Reverse Vowels of a String
def reverseVowels(s: str) -> str:
        arr = list(s)
        vowels = 'aeiouAEIOU'
        i = 0
        j = len(s) - 1
        while i < j:
            if arr[i] not in vowels:
                i += 1
            elif arr[j] not in vowels:
                j -= 1
            else:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
                j -= 1
        return ''.join(arr)

s = "IceCreAm"
print(reverseVowels(s))