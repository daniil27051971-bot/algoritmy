class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def sorted_array_to_bst(nums):
    def helper(left, right):
        if left > right:
            return None
        
        mid = (left + right) // 2
        node = TreeNode(nums[mid])
        
        node.left = helper(left, mid - 1)
        node.right = helper(mid + 1, right)
        
        return node
    
    return helper(0, len(nums) - 1)

arr = [17, 6, 5, 20, 19, 18, 11, 14, 12, 13, 2, 4, 10]
nums = sorted(arr)  # Обязательная сортировка
root = sorted_array_to_bst(nums)

def inorder(node, res):
    if not node:
        return
    inorder(node.left, res)
    res.append(node.val)
    inorder(node.right, res)

result = []
inorder(root, result)
print("In-order обход:", result)