#19. Remove Nth Node From End of List

#Fake Node
class Node:
    def __init__(self, num):
        self.num = num
        self.right = self
        self.left = self

class List:
    def __init__(self, last, first):
        self.last = last
        self.first = first

class Solution:
    def removeNthNodeFromEndOfList(self, list, n):
        #check if remove the first or the last node
        #if remove the last node

        length = 0
        tempNode = list.last

        while tempNode:
            tempNode = tempNode.left
            length += 1

        if n == 1:
            list.last = list.last.left
            list.last.right = None
        elif n == length:
            list.first = list.first.right
            list.first.left = None
        else:
            # Node : length - n should be deleted
            counter = 1
            tempNode = list.last
            while counter < n:
                counter += 1
                tempNode = tempNode.left
            tempNode.right.left = tempNode.left
            tempNode.left.right = tempNode.right

list = []
for i in range(10):
    list.append(Node(i + 1))
for i in range(len(list)):
    if i == 0:
        list[i].right = list[i + 1]
        list[i].left = None
    elif i == len(list) - 1:
        list[i].left = list[i - 1]
        list[i].right = None
    else:
        list[i].left = list[i - 1]
        list[i].right = list[i + 1]

cycle = List(list[len(list) - 1], list[0])

Solution().removeNthNodeFromEndOfList(cycle, 1)

tempNode = cycle.last
while tempNode:
    print(tempNode.num)
    tempNode = tempNode.left