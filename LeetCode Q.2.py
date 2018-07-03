'''
Add Two Numebrs
'''
'''
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Solution:
    def addTwoNumebrs(self, l1, l2):
        quot = 0
        p = ListNode(0)
        sum = p
        while l1 or l2 or quot != 0:
            if l1:
                quot += l1.value
                l1 = l1.next
            if l2:
                quot += l2.value
                l2 = l2.next
            quot = quot // 10 #进位
            rem = quot % 10 #余数
            sum.next = ListNode(rem)
            sum = sum.next
        return p
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)
        p = head
        quot = 0
        while l1 or l2 or quot != 0:
            if l1:
                quot += l1.val
                l1 = l1.next
            if l2:
                quot += l2.val
                l2 = l2.next
            quot, rem = divmod(quot, 10)
            p.next = ListNode(rem)
            p = p.next

        return head.next

def compareLinkedList(l1, l2):
    while l1 or l2:
        if (not (l1 and l2)) or l1.val != l2.val:
            return False
        l1 = l1.next
        l2 = l2.next
    return True

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    lsum = ListNode(7)
    lsum.next = ListNode(0)
    lsum.next.next = ListNode(8)
    print(compareLinkedList(Solution().addTwoNumbers(l1, l2), lsum))