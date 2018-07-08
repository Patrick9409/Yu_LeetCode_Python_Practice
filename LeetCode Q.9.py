'''
Palindrome Number
'''
class Solution:
    def palindromeNumber(self, num):
        if num < 0: #-121 -> 121-
            return False
        else:
            arr = []
            while num != 0:
                val = num % 10
                num = num // 10
                arr.append(val)
            for i, j in zip(range(len(arr)), range(len(arr))):
                if i <= j:
                    if arr[i] != arr[::-1][j]:
                        return False
            return True

print(Solution().palindromeNumber(123321))
