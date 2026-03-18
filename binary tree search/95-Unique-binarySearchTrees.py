class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Answer:
    def generateTrees(self, n):
        if n == 0:
            return []

        def create(start, end):
            if start > end:
                return [None]

            trees = []

            for i in range(start, end + 1):
                left_trees = create(start, i - 1)
                right_trees = create(i + 1, end)

                for left in left_trees:
                    for right in right_trees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return create(1, n)