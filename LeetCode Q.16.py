#16. 3Sum Closest
class Solution:
    def threeSumClosest(self, list, target):
        sum = list[0] + list[1] + list[2]
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                for k in range(j + 1, len(list)):
                    if list[i] + list[j] + list[k] > target:
                        if list[i] + list[j] + list[k] < sum:
                            sum = list[i] + list[j] + list[k]
                    else:
                        if list[i] + list[j] + list[k] > sum:
                            sum = list[i] + list[j] + list[k]
        return sum

list = [-1, 2, 1, -4]
target = 1
print(Solution().threeSumClosest(list, target))