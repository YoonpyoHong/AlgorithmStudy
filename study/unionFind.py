import sys

union = []

def findParent(node):
    if union[node] == node:
        return node
    return findParent(union[node])

def unionSets(nodeX, nodeY):
    if nodeX > nodeY:
        union[nodeX] = nodeY
    else:
        union[nodeY] = nodeX