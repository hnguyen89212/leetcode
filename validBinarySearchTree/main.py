class Node(object):
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

class Solution(object):
    def _isValidBSTHelper(self, node, low, high):
      if not node: return True
      value = node.value
      if ((low < value and value < high)
            and (self._isValidBSTHelper(node.left, low, value))
            and (self._isValidBSTHelper(node.right, value, high))
          ):
          return True
      return False

    def isValidBST(self,node):
      return self._isValidBSTHelper(node, float('-inf'), float('inf'))

#   5
#  / \
# 4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#   5
#  / \
# 4   7
#    /
#   2
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(2)
print(Solution().isValidBST(node))
# False
