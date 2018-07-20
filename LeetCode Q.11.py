#11. Container With Most Water

class Solution:
    def containerWithMostWater(self, list):
        area = 0 #area of container
        pointer1 = 0
        pointer2 = 0
        for i in range(len(list)):
            for j in range(i + 1, len(list)):
                tempArea = (j - i) * (list[i] + list[j]) / 2
                if tempArea > area:
                    area = tempArea
                    pointer1 = i
                    pointer2 = j
        return pointer1 + 1, pointer2 + 1

list = [1, 2, 3, 4, 5, 6, 7, 8, 7, 6, 5, 4, 3, 2, 1]
pointer1, pointer2 = Solution().containerWithMostWater(list)
print(str(pointer1) + '->' + str(list[pointer1 - 1]) + ' and ' + str(pointer2) + '->' + str(list[pointer2 - 1]))