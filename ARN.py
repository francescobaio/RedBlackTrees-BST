from ABR import *


class ARNNode(ABRNode):

    def __init__(self, key=0, colour="BLACK"):
        super().__init__(key)
        self.colour = colour


class ARN(ABR):

    def __init__(self):
        # i valori dei campi della sentinella sono irrilevanti
        super().__init__()
        self.nil = ARNNode()
        self.nil.color = "BLACK"
        self.root = self.nil

    def setRoot(self, key):
        self.root = ARNNode(key)
        self.root.color = "BLACK"
        self.root.parent = self.nil

    def leftRotate(self, x):
        y = x.right
        x.right = y.left
        if y.left is not self.nil:
            y.left.p = x
        y.p = x.p
        if x.p == self.nil:
            self.root = y
        elif x == x.p.left:
            x.p.left = y
        else:
            x.p.right = y
        y.left = x
        x.p = y

    def rightRotate(self, y):

        x = y.left
        y.left = x.right
        if x.right != self.nil:
            x.right.p = y
        x.p = y.p
        if y.p is self.nil:
            self.root = x
        elif y is y.p.left:
            y.p.left = x
        else:
            y.p.right = x
        x.right = y
        y.p = x

    def insertFixUp(self, z):
        while z.p.colour == "RED":
            if z.p is z.p.p.left:
                y = z.p.p.right
                if y.colour == "RED":
                    z.p.colour = "BLACK"
                    y.colour = "BLACK"
                    z.p.p.colour = "RED"
                    z = z.p.p
                else:
                    if z == z.p.right:
                        z = z.p
                        self.leftRotate(z)
                    z.p.colour = "BLACK"
                    z.p.p.colour = "RED"
                    self.rightRotate(z.p.p)
            else:
                y = z.p.p.left
                if y.colour == "RED":
                    z.p.colour = "BLACK"
                    y.colour = "BLACK"
                    z.p.p.colour = "RED"
                    z = z.p.p
                else:
                    if z == z.p.left:
                        z = z.p
                        self.rightRotate(z)
                    z.p.colour = "BLACK"
                    z.p.p.colour = "RED"
                    self.leftRotate(z.p.p)
        self.root.colour = "BLACK"

    def insert(self, key):

        z = ARNNode(key)
        y = self.nil
        x = self.root
        while x is not self.nil:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y is self.nil:
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

        z.left = self.nil
        z.right = self.nil
        z.colour = "RED"
        self.insertFixUp(z)


