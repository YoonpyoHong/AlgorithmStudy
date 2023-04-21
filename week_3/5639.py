import sys
sys.setrecursionlimit(100000)

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

inputArr = []

while True:
    try:
        num = sys.stdin.readline()
        inputArr.append(int(num.rstrip()))
    except:
        break

def buildBST(preorder):
    if not preorder:
        return
    root = Node(preorder[0])
    if len(preorder) ==1:
        return root
    index = 1
    while index < len(preorder) and preorder[index] < root.val:
        index+=1

    root.left = buildBST(preorder[1:index])
    root.right = buildBST(preorder[index:])
    
    return root

root = buildBST(inputArr)

def thirdsearch(node):
    if node.left:
        thirdsearch(node.left)
    if node.right:
        thirdsearch(node.right)
    sys.stdout.write(str(node.val) + "\n")

thirdsearch(root)

