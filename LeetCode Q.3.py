'''
Longest Substring Without Repeating Characters
'''
class Solution:
    def longestSubstring(self, str):
        length = 0 #record length of substring
        subString = str[0] #record the substring
        for i in range(len(str) - 1): #i used to locate the first pointer
            tempStr = str[i] #temporary record the substring
            for j in range(i + 1, len(str)): #j used to locate the second pointer
                tempStrAppend = True
                for k in tempStr: #k used to compare the second pointer with the temporary recorded substring
                    if str[j] == k: #check if tempStr include str[j]
                        tempStrAppend = False
                        break #if include, break loop for J, jump to loop for i
                if tempStrAppend:
                    tempStr += str[j]
                    if len(tempStr) >length:
                        length = len(tempStr)
                        subString = tempStr
                else:
                    break
        return subString

print(Solution().longestSubstring('pwwkew'))
print(Solution().longestSubstring('bbbbbb'))
print(Solution().longestSubstring('abcabcbb'))
