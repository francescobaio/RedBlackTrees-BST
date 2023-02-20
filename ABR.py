class ABRNode:
    def __init__(self, key=None):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

    def get(self):
        return self.key

    def set(self, key):
        self.key = key

    def getChildren(self):
        children = []
        if (self.left != None):
            children.append(self.left)
        if (self.right != None):
            children.append(self.right)
        return children


class ABR:
    def __init__(self):
        self.root = None

    def setRoot(self, key):
        self.root = ABRNode(key)

    def search(self, key):
        if self.root is None:
            return False
        x = self.root
        while x.key != key:
            if key > x.key:
                if x.right is None:
                    return False
                x = x.right
            else:
                if x.left is None:
                    return False
                x = x.left
        return True

    def findMinimum(self, x):
        while x.left is not None:
            x = x.left
        return x

    def findMaximum(self, x):
        while x.right is not None:
            x = x.right
        return x

    def insert(self, key):
        if self.root is None:
            self.setRoot(key)
        else:
            y = None
            x = self.root
            z = ABRNode(key)

            while x is not None:
                y = x
                if z.key < x.key:
                    x = x.left
                else:
                    x = x.right
            z.p = y
            if y is None:
                self.root = z
            elif z.key < y.key:
                y.left = z
            else:
                y.right = z

    def successor(self, x):
        if x.right is not None:
            return self.findMinimum(x.right)
        else:
            y = x.p
            while y is not None and x is y.right:
                x = y
                y = y.p
            return y

    def predecessor(self, x):
        if x.left is not None:
            return self.findMaximum(x.left)
        else:
            y = x.p
            while y is not None and x is y.left:
                x = y
                y = y.p
            return y

    def transplant(self, x, v):
        if x is self.root:
            self.root = v
        elif x is x.p.left:
            x.p.left = v
        else:
            x.p.right = v
        if v is not None:
            v.p = x.p

    def delete(self, z):
        if z is None:
            return None
        elif z.left is None:
            # gestisce anche il caso in cui z non ha figli
            self.transplant(z, z.right)
        elif z.right is None:
            self.transplant(z, z.left)
        else:
            y = self.findMinimum(z.right)
            if y is not z.right:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.p = y

            self.transplant(z, y)
            y.left = z.left
            z.left.p = y

    def getNodeHeight(self, x):
        height = 0
        if x is None:
            return height
        else:
            left_height = self.getNodeHeight(x.left)
            right_height = self.getNodeHeight(x.right)
            return 1 + max(left_height, right_height)

    def getHeight(self):
        height = 0
        if self.root is None:
            return height
        height = self.getNodeHeight(self.root)
        if height == 0:
            return 0
        else:
            return height - 1
