#22. Generate Parentheses

class Solution:
    def generateParentheses(self, n):
        def generate(list = []):
            if len(list) == 2 * n:
                if valid(list):
                    returnList.append(''.join(list))
            else:
                list.append('(')
                generate(list)
                list.pop()
                list.append(')')
                generate(list)
                list.pop()

        def valid(list):
            balance = 0
            if list[0] != '(':
                return False
            elif list[len(list) - 1] != ')':
                return False
            else:
                for i in list:
                    if i == '(':
                        balance += 1
                    else:
                        balance -= 1
                    if balance < 0:
                        return False
                return balance == 0

        returnList = []
        generate()
        return returnList

print(Solution().generateParentheses(3))