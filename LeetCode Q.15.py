'''
15. 3sum

class Solution:
    def threeSum(self, list, sum):
        list.sort()
        list1 = []
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                for k in range(j + 1, len(list)):
                    if list[i] + list[j] + list[k] == sum:
                        list1.append([list[i], list[j], list[k]])
        for i in range(len(list1)):
            for j in range(i + 1, len(list1)):
                if list1[i] == list1[j]:
                    del list1[j]
        return list1

list = [-1, 0, 1, 2, -1, -4]
print(Solution().threeSum(list, 0))
'''

#15. 3sum solution 2
class Solution:
    def threeSum(self, list, target):
        returnList = []
        if len(list) < 3:
            return list
        else:
            list.sort()
            for i in range(len(list) - 2):
                twoSum = target - list[i]
                if list[i] == list[i + 1]:
                    i += 1
                else:
                    a = i + 1
                    b = len(list) - 1
                    while a < b:
                        if list[a] + list[b] == twoSum:
                            returnList.append([list[i], list[a], list[b]])
                            a += 1
                            b -= 1
                            while list[a] == list[a - 1]:
                                a += 1
                            while list[b] == list[b + 1]:
                                b -= 1
                        elif list[a] + list[b] < twoSum:
                            a += 1
                        else:
                            b -= 1
        return returnList
list = [-2, -1, 0, 1, 2, 4]
print(Solution().threeSum(list, 0))