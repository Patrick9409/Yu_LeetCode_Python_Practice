'''
Longest Palindromic Substring
'''
class Solution:
    def longestPalindromicSubstring(self, str):
        subString = ''
        for i in range(1, len(str) - 1):
            #Two Conditions: abba/abcba
            #First Condition: abba, i stands for first b and i + 1 stands for second b
            if str[i] == str[i + 1]:
                tempString = ''
                for j in range(i + 1):
                    if i + 1 + j < len(str): #biggest pointer is in the range
                        if str[i - j] == str[i + j + 1]:
                            tempString = str[i - j] + tempString + str[i + j + 1]
                            if 2 * j + 2 > len(subString):
                                subString = tempString
                        else:
                            break
            #Second Condition: abcba, i stands for c, i - 1 and i + 1 stands for b
            if str[i - 1] == str[i + 1]:
                tempString = str[i]
                for j in range(i):
                    if i + 1 + j < len(str):
                        if str[i - j - 1] == str[i + j + 1]:
                            tempString = str[i - 1 - j] + tempString + str[i + 1 + j]
                            if 2 * j + 3 > len(subString):
                                subString = tempString
                        else:
                            break
        return subString
print(Solution().longestPalindromicSubstring('abeba'))