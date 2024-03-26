class Node:    
    def __init__(self, left_child, right_child):
        self.left_child = left_child
        self.right_child = right_child
      
    def height(self):
        if self.left_child:
            h_left = 1+self.left_child.height()
        else:
            h_left = 0
        if self.right_child:
            h_right = 1+self.right_child.height()
        else:
            h_right = 0
        return max(0, h_left, h_right)


      
if __name__ == "__main__":
    leaf1 = Node(None, None)
    leaf2 = Node(None, None)
    node = Node(leaf1, None)
    root = Node(node, leaf2)
    
    print(root.height())