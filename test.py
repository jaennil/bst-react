

class TreeNode:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
        self.depth = 0
        self.calculateDepth(self)
        if self.parent:
            self.x = self.parent.x
            self.y = self.parent.y + 100
        else:
            self.x = 1920 // 2
            self.y = 40

    def hasleft(self):
        return self.left

    def hasright(self):
        return self.right

    def isleft(self):
        return self.parent and self.parent.left == self

    def isright(self):
        return self.parent and self.parent.right == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.right or self.left)

    def hasAnyChildren(self):
        return self.right or self.left

    def hasBothChildren(self):
        return self.right and self.left

    def calculateDepth(self, node):
        if node.parent:
            self.depth += 1
            self.calculateDepth(node.parent)


class BSTree:
    def __init__(self, canvas=None):
        self.canvas = canvas
        self.root = None

    def insert(self, value):
        if self.root:
            self._insert(value=value, node=self.root)
        else:
            self.root = TreeNode(value=value)
            if self.canvas:
                self.canvas.create_oval(
                    self.root.x - 10,
                    self.root.y - 10,
                    self.root.x + 10,
                    self.root.y + 10,
                    fill="yellow",
                )
                self.canvas.create_text(self.root.x, self.root.y, text=self.root.value)

    def _insert(self, value, node):
        if value < node.value:
            if node.hasleft():
                self._insert(value, node.left)
            else:
                node.left = TreeNode(value, parent=node)
                node.left.x -= 100
                if self.canvas:
                    self.canvas.create_oval(
                        node.left.x - 10,
                        node.left.y - 10,
                        node.left.x + 10,
                        node.left.y + 10,
                        fill="yellow",
                    )
                    self.canvas.create_text(node.left.x, node.left.y, text=node.left.value)
        elif value > node.value:
            if node.hasright():
                self._insert(value, node.right)
            else:
                node.right = TreeNode(value, parent=node)
                node.right.x += 100
                if self.canvas:
                    self.canvas.create_oval(
                        node.right.x - 10,
                        node.right.y - 10,
                        node.right.x + 10,
                        node.right.y + 10,
                        fill="yellow",
                    )
                    self.canvas.create_text(
                        node.right.x, node.right.y, text=node.right.value
                    )

        else:
            print("Node exist")

    def print_tree_inOrder(self):
        if self.root is not None:
            self._print_tree_inOrder(self.root)
        else:
            print("Tree Is Empty")

    def _print_tree_inOrder(self, node):
        if node is not None:
            self._print_tree_inOrder(node.left)
            print(node.value)
            self._print_tree_inOrder(node.right)

    def print_tree_postOrder(self):
        if self.root is not None:
            self._print_tree_postOrder(self.root)
        else:
            print("Tree Is Empty")

    def _print_tree_postOrder(self, node):
        if node is not None:
            self._print_tree_postOrder(node.left)
            self._print_tree_postOrder(node.right)
            print(node.value)

    def maxim(self):
        if not self.root:
            print("Tree Is Empty")
        else:
            self._maxim(self.root)

    def _maxim(self, node):
        if node.hasright():
            self._maxim(node.right)
        else:
            print(node.value)

    def minim(self):
        if not self.root:
            print("Tree Is Empty")
        else:
            self._minim(self.root)

    def _minim(self, node):
        if node.hasleft():
            self._minim(node.left)
        else:
            print(node.value)

    def search(self, value, node):
        if not node:
            pass
        elif node.value == int(value):
            self.search_bool = True
        elif node.value > int(value):
            self.search(value, node.left)
        elif node.value < int(value):
            self.search(value, node.right)

    def print_tree_preOrder(self):
        if self.root is not None:
            self._print_tree_preOrder(self.root)
        else:
            print("Tree Is Empty")

    def _print_tree_preOrder(self, node):
        if node:
            print(node.value)
            self._print_tree_preOrder(node.left)
            self._print_tree_preOrder(node.right)

    def height(self, node):
        if not node:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    def get_size(self):
        if self.root:
            self.size = self._get_size(self.root)
            print(self.size)
        else:
            print("Tree Is Empty")

    def _get_size(self, node):
        if not node:
            return 0
        else:
            return self._get_size(node.left) + self._get_size(node.right) + 1

bst = BSTree()
bst.insert(10)
bst.insert(100)
bst.insert(120)
bst.insert(50)
bst.insert(5)
bst.insert(4)
bst.insert(6)
bst.print_tree_inOrder()

# def buttonCommand():
#     bst.insert(entry_var.get())
#     print(f"{entry_var.get() = }")
#     print(f"{type(entry_var.get()) = }")
#     print("button command")


# import tkinter as tk

# root = tk.Tk()
# root.geometry("1920x1080")
# canvas = tk.Canvas(master=root, width=1920, height=1080, bg="blue")
# canvas.pack(fill=tk.BOTH, expand=True)
# entry_var = tk.IntVar()
# entry = tk.Entry(master=canvas, textvariable=entry_var)
# entry.grid(row=0, column=0)
# button = tk.Button(master=canvas, text="input", command=buttonCommand)
# button.grid(row=0, column=1)
# bst = BSTree(canvas)
# root.mainloop()
