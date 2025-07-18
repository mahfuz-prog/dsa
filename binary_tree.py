from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# pre_order = [1,2,-1,-1,4,-1,-1]
# pre_order = [1,2,-1,-1,3,4,-1,-1,5,-1,-1]
pre_order = [1,2,4,-1,-1,5,-1,-1,3,6,-1,-1,7,-1,-1]

idx = -1
def build_tree(pre_order):
    global idx
    idx += 1
    if pre_order[idx] == -1:
        return None

    # build root node
    root = TreeNode(pre_order[idx])

    # recursive leap of faith
    root.left = build_tree(pre_order)
    root.right = build_tree(pre_order)

    return root

root = build_tree(pre_order)
print("Build tree:", root)


# ===================================
# pre order traversal, BFS
# fashion: root -> left -> right
# tc O(n)

def traverse_pre_order(root, ans):
    if not root:
        ans.append("*")
        return
    
    ans.append(root.val)
    traverse_pre_order(root.left, ans)
    traverse_pre_order(root.right, ans)

ans = []
traverse_pre_order(root, ans)
print("Pre order traversal:", ans)


# =====================================
# in order traversal, BFS
# fashion: left -> root -> right
# tc O(n)

def traverse_in_order(root, ans):
    # currnent node
    if not root:
        return

    traverse_in_order(root.left, ans)
    ans.append(root.val)
    traverse_in_order(root.right, ans)

ans = []
traverse_in_order(root, ans)
print("In order traversal:", ans)


# ======================================
# post order traversal, BFS
# fashion: left -> right -> root
# tc O(n)

def traverse_post_order(root, ans):
    # currnent node
    if not root:
        return

    traverse_post_order(root.left, ans)
    traverse_post_order(root.right, ans)
    ans.append(root.val)

ans = []
traverse_post_order(root, ans)
print("Post order traversal:", ans)
print()


# ======================================
# level order traversal, DFS
# tc O(n)

q = deque()
q.append(root)
q.append(None)

print("-------------level order-----------------")
while q:
    current_node = q.popleft()

    if current_node:
        print(current_node.val, end=" ")

        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
    else:
        print()

        if q:
            q.append(None)
print("-------------level order-----------------")
print()


# ================================================
# height of tree
# calculate height post order
# tc O(n)

def height(root):
    if not root:
        return 0

    left_height = height(root.left)
    right_height = height(root.right)

    return max(left_height, right_height) + 1

h = height(root)
print("height:", h)


# ===============================================
# diameter
# max diameter could include root
# it could also exist in left or right

# approach 1
def diameter_1(root):
    if not root:
        return 0
    
    # calculate height for left subtree and right subtree
    left_diameter = height(root.left)
    right_diameter = height(root.right)
    current_diameter = left_diameter + right_diameter
    return max(current_diameter, max(left_diameter, right_diameter))

d = diameter_1(root)
print("Diameter of tree 1:", d)

# approach 2
# tc O(n), Sc O(n)/O(logn)
ans = 0
def diameter_2(root):
    global ans
    if not root:
        return 0

    left_height = diameter_2(root.left)
    right_height = diameter_2(root.right)

    # track maximum diameter (left_height + right_height)
    ans = max(ans, (left_height + right_height))

    # calculate height for smaller portion
    return max(left_height, right_height) + 1

diameter_2(root)
print("Diameter of tree 2:", ans)


# ================================================
# count

def count(root):
    if not root:
        return 0

    left_count = count(root.left)
    right_count = count(root.right)

    return left_count + right_count + 1

c = count(root)
print("Count: ", c)


# =======================================================
# top view of a tree

def top_view(root):
    res = {}
    q = deque()
    q.append((0, root))

    while q:
        distance, current_node = q.popleft()

        if current_node.left:
            q.append((distance - 1 ,current_node.left))

        if current_node.right:
            q.append((distance + 1 ,current_node.right))

        # if the distance already exist that mean it shows from top
        if distance not in res:
            res[distance] = current_node.val

    return res

res = top_view(root)
print("Top view:", end=" ")
for i in sorted(res):
    print(res[i], end=" - ")
print()


# =================================================
# bottom view

def bottom_view(root):
    res = {}
    q = deque()
    q.append((0, root))

    while q:
        distance, current_node = q.popleft()
        # keep updating distance to get last seen element
        res[distance] = current_node.val

        if current_node.left:
            q.append((distance - 1 ,current_node.left))

        if current_node.right:
            q.append((distance + 1 ,current_node.right))

    return res

res = bottom_view(root)
print("Bottom view:", end=" ")
for i in sorted(res):
    print(res[i], end=" - ")
print()

# ==================================================
# k-th level of a bin tree, recursive
# decrease k in every level. k == 1 is target level
print("kth level:", end=" ")
def kth_level(root, k):
    if not root:
        return

    if k == 1:
        print(root.val, end=" ")
        return

    kth_level(root.left, k-1)
    kth_level(root.right, k-1)

kth_level(root, 3)


# ==================================================
# sum tree
def sum_tree(root):
    if not root:
        return 0

    left_sum = sum_tree(root.left)
    right_sum = sum_tree(root.right)

    root.val += left_sum + right_sum

    return root.val

# sum_tree(root)
print()
def traverse_pre_order(root):
    if not root:
        return
    
    print(root.val, end=" ")
    traverse_pre_order(root.left)
    traverse_pre_order(root.right)

# traverse_pre_order(root)