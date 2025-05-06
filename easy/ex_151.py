
# # 151. Reverse Words in a String
def reverseWords(s: str) -> str:
        arr = s.split()
        i = 0
        j = len(arr) - 1
        while i < j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        return ' '.join(arr)

s = "the sky is blue"
print(reverseWords(s))