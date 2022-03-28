``` Python

class BST:


    class Node:


        def __init__(self, data):
       
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):

        self.root = None

    def insert(self, data):

        if self.root is None:
        
            self.root = BST.Node(data)
            
        else:
        
            self._insert(data, self.root)  # Start at the root

    def _insert(self, data, node):

        if data < node.data:
     
            if node.left is None:
 
                node.left = BST.Node(data)
                
            else:
  
                self._insert(data, node.left)
            else:
   
                node.right = BST.Node(data)
            else:

                self._insert(data, node.right)

```
