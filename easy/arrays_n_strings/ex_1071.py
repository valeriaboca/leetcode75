
# 1071. Longest Common Divisor of Strings
def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ''
        
        def gcd(len_gcd1, len_gcd2):
            while len_gcd2:
                len_gcd1, len_gcd2 = len_gcd2, len_gcd1 % len_gcd2
            return len_gcd1

        gcdStr = gcd(len(str1), len(str2))
        return str1[:gcdStr]

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))