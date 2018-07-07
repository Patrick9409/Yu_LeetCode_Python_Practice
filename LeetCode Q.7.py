'''
Reverse Integer
'''
class Solution:
    def reverseInteger(self, number):
        reverseString = ''
        coveredStr = str(number)
        if number >= 0: #without '-'
            for i in coveredStr:
                reverseString = i + reverseString
        else: #with '-'
            for i in coveredStr:
                if i != '-':
                    reverseString = i + reverseString
            reverseString = '-' + reverseString
        return int(reverseString) if -0X7fffffff <= int(reverseString) <= 0X7fffffff else 0

print(Solution().reverseInteger(-12111100000001))