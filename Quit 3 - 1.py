class Kid:
    id = 0
    def __init__(self):
        self.left = self
        self.right = self

class KidCircle:

    count = 0
    first = Kid()
    last = Kid()

    def __init__(self, n):
        for i in range(n):
            self.add()

    def add(self):
        k = Kid()
        k.id = self.count
        if self.count <= 0 :
            self.first = k
            self.last = k
            k.left = k
            k.right = k
        else:
            self.last.right = k
            k.right = self.first
            k.left = self.last
            self.first.left = k
            self.last = k
        self.count += 1

    def delete(self, k):
        if self.count <= 0:
            print('no kids to delete')
        elif self.count == 1:
            self.first = self.last = None
        else:
            k.left.right = k.right
            k.right.left = k.left
            if k == self.last:
                self.last = k.left
            elif k == self.first:
                self.first = k.right
        self.count -= 1

if __name__ == "__main__":
    kc = KidCircle(100)
    countNum = 0
    k = kc.first
    while kc.count > 1:
        countNum += 1
        if countNum == 3:
            kc.delete(k)
            countNum = 0
        k = k.right
    print(kc.first.id)