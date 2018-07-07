'''
ZigZag Conversion
'''

'''
        1                                       1             
            2                               10      2
                3                       9
                    4               8
                        5       7
                            6
                            |
                            V
        1                                       1
            2                               2       2
                3                       3
                    4               4
                        5       5
                            6
'''

class Solution:
    def zigzagConversion(self, str, rowNum):
        # condition of the repeating character
        array = []
        arrayStr = []
        for i in range(len(str)):
            if (i + 1) % (2 * rowNum - 2) == 0:
                array.insert(i, 2)
                arrayStr.insert(i, str[i])
            elif (i + 1) % (2 * rowNum - 2) > rowNum:
                array.insert(i, 2 * rowNum - (i + 1) % (2 * rowNum - 2))
                arrayStr.insert(i, str[i])
            else:
                array.insert(i, (i + 1) % (2 * rowNum - 2))
                arrayStr.insert(i, str[i])
        max = 0
        str = ''
        for i in array:
            if i > max:
                max = i
        for i in range(max + 1):
            for j in range(len(array)):
                if array[j] == i:
                    str += arrayStr[j]
        return str

print(Solution().zigzagConversion('PAYPALISHIRING', 4))