#18 4Sum // stack not enough, without testing

class Solution:
    def fourSum(self, list, target):
        tempList = []
        if len(list) < 4:
            return list
        else:
            list.sort()
            for i in range(len(list)):
                for j in range(len(list))[::-1]:
                    while i < j:
                        twoSum = target - list[i] - list[j]
                        a = i + 1
                        b = j - 1
                        while a < b:
                            if list[a] + list[b] == twoSum:
                                tempList.append([i, a, b, j])
                                while list[a] == list[a + 1]:
                                    a += 1
                                while list[b] == list[b - 1]:
                                    b -= 1
                                a += 1
                                b -= 1
                            elif list[a] + list[b] < twoSum:
                                a += 1
                            else:
                                b -= 1
                        while list[i] == list[i + 1]:
                            i += 1
                        while list[j] == list[j - 1]:
                            j -= 1
            return tempList

list = [1, 0, -1, 0, -2, 2]
print(Solution().fourSum(list, 0))