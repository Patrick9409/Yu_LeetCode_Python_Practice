#17. Letter Combinations of a Phone Number

# 2: abc 3: def 4: ghi 5: jkl 6: mno 7: pqrs 8: tuv 9: wxyz
class Solution:
    def letterCombinationsOfAPhoneNumber(self, number):
        num = str(number)
        dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        list = []
        for i in num:
            tempList = list[:]
            list.clear()
            if tempList:
                for j in range(len(tempList)):
                    for k in dict.get(i):
                        list.append(tempList[j] + k)
            else:
                for j in dict.get(i):
                    list.append(j)
        return list

print(Solution().letterCombinationsOfAPhoneNumber(27))