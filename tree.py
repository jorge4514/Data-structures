class Tree:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def sumRange(tree, rangeMin, rangeMax):
    if(tree == None):
        return 0
    current_node = tree.value

    if(current_node >= rangeMin and current_node <= rangeMax):
        return current_node + sumRange(tree.left, rangeMin, rangeMax) + sumRange(tree.right, rangeMin, rangeMax)
    elif(current_node > rangeMax):
        return sumRange(tree.left, rangeMin, rangeMax)
    else:
        return sumRange(tree.right, rangeMin, rangeMax)

tree = Tree(5, Tree(3, None, Tree(4, None, None)), Tree(7, None, None)) 

print(sumRange(tree, 3, 4))