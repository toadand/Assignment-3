from numpy import deprecate_with_doc


class TreeNode:
    def __init__(self, e):
      self.element = e
      self.left = None # Point to the left node, default None
      self.right = None # Point to the right node, default None


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    # Return True if the element is in the tree
    def search(self, e):
        current = self.root # Start from the root

        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else: # element matches current.element
                return True # Element is found

        return False

    # Insert element e into the binary search tree
    # Return True if the element is inserted successfully
    def insert(self, e):
        if self.root == None:
          self.root = self.createNewNode(e) # Create a new root
        else:
          # Locate the parent node
          parent = None
          current = self.root
          while current != None:
            if e < current.element:
              parent = current
              current = current.left
            elif e > current.element:
              parent = current
              current = current.right
            else:
              return False # Duplicate node not inserted

          # Create the new node and attach it to the parent node
          if e < parent.element:
            parent.left = self.createNewNode(e)
          else:
            parent.right = self.createNewNode(e)

        self.size += 1 # Increase tree size
        return True # Element inserted

    # Create a new TreeNode for element e
    def createNewNode(self, e):
      return TreeNode(e)


    def getSuccessor(self, current):
      while current.left != None:
        current = current.left
      return current

    def getPredecessor(self, current):
      while current.right != None:
        current = current.right
      return current

    """
    " DELETE METHOD
    " 4 CASES TO CONSIDER WHEN DELETING NODE k:
    " 1) NODE HAS NO CHILDREN (IS A LEAF NODE) - SIMPLY DELETE NODE k
    " 2) NODE HAS 1 LEFT CHILD - REPLACE k WITH CHILD
    " 3) NODE HAS 1 RIGHT CHILD - REPLACE k WITH CHILD
    " 2) NODE HAS 2 CHILDREN - REPLACE k WITH IN ORDER SUCCESSOR
    " WRITTEN BY JACK ELLIS
    """
    def delete(self, key):
        self.deleteHelper(self.root, key)
  
    def deleteHelper(self, current, key):        
        # key node not found in tree
        if current == None:
            return "Error: node not found in tree"

        # current node is the key to delete
        if current.element == key:
            # case 1 - node has no children
            # simply delete the node
            if current.left == None and current.right == None:
                print(f'\nNode {key} has no children and is simply deleted.')
                current = None
                    
            # case 2 - node has 1 right child
            # replace node with its child
            elif current.left == None:
                print(f'\nNode {key} has 1 right child.')
                print(f'Replacing {key} with right child {current.right.element}')
                child = current.right
                print('Deleting original child node...', end='')
                self.deleteHelper(current, current.right.element)
                current = child
            # case 3 - node has 1 left child
            # replace node with its child
            elif current.right == None:
                print(f'\nNode {key} has 1 left child.')
                print(f'Replacing {key} with left child {current.left.element}')
                child = current.left
                print('Deleting original child node...', end='')
                self.deleteHelper(current, current.left.element)
                current = child
            # case 4 - node has 2 children
            # replace current node with its successor
            # (smallest element of the right subtree)
            else:
                ##case 2 - deleting topmost element of subtree
                ##find the leftmost element of right subtree and insert at top position
                print(f'\nNode {key} has 2 children.')
                successor = self.getSuccessor(current.right)
                print(f'Replacing {key} with successor {successor.element}')
                print('Deleting original successor node...', end='')
                self.deleteHelper(current, successor.element)
                current.element = successor.element

        # else recursively call the function until the node is found
        elif key < current.element:
            current.left = self.deleteHelper(current.left, key)
        else:
            current.right = self.deleteHelper(current.right, key)
        return current
    
    # Return the size of the tree
    def getSize(self):
      return self.size

    # Inorder traversal from the root
    def inorder(self):
      self.inorderHelper(self.root)

    # Inorder traversal from a subtree
    def inorderHelper(self, r):
      if r != None:
        self.inorderHelper(r.left)
        print(r.element, end = " ")
        self.inorderHelper(r.right)


    """
    " PRINT LEAF NODES METHOD
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES ARE TRAVERSED (IN ORDER)
    " AND ALL LEAF NODES ARE PRINTED
    " WRITTEN BY JACK ELLIS
    """
    def printLeafNodes(self):
        self.printLeafNodeHelper(self.root)

    def printLeafNodeHelper(self, r):
        if r!= None:
            self.printLeafNodeHelper(r.left)
            if not r.left and not r.right:
                #i.e. has no child and is therefore a leaf node
                print(r.element, end = " ")
            self.printLeafNodeHelper(r.right)

    """
    " PRINT NON LEAF NODES METHOD
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES ARE TRAVERSED (IN ORDER)
    " AND ALL NON LEAF NODES ARE PRINTED
    " WRITTEN BY JACK ELLIS
    """
    def printNonLeafNodes(self):
        self.printNonLeafNodeHelper(self.root)

    def printNonLeafNodeHelper(self, r):
        if r!= None:
            self.printNonLeafNodeHelper(r.left)
            if r.left or r.right:
                #i.e. has a child and is therefore not a leaf node
                print(r.element, end = " ")
            self.printNonLeafNodeHelper(r.right)


    # Postorder traversal from the root
    def postorder(self):
      self.postorderHelper(self.root)

    # Postorder traversal from a subtree
    def postorderHelper(self, root):
      if root != None:
        self.postorderHelper(root.left)
        self.postorderHelper(root.right)
        print(root.element, end = " ")


    """
    " GET SUBTREE DEPTH
    " FIRST FINDS NODE N IN THE BST
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES OF N'S SUBTREES ARE TRAVERSED (POST ORDER)
    " THEREFORE CALCULATING THE DEPTH OF N'S SUBTREE
    " WRITTEN BY CHRIS HODDER
    """
    def getSubtreeDepth(self, e):
        # first search for node e in the BST
        current = self.root
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                # once node e is found
                depth = self.getSubtreeDepthHelper(current)
                return depth
        # if node e not found
        print(f'Node {e} not found.')

    def getSubtreeDepthHelper(self, root):
      if root.left and root.right:
        return 1 + max(self.getSubtreeDepthHelper(root.left), self.getSubtreeDepthHelper(root.right))
      elif root.left:
        return 1 + self.getSubtreeDepthHelper(root.left)
      elif root.right:
        return 1 + self.getSubtreeDepthHelper(root.right)
      else:
        return 1

    """
    " GET NODE DEPTH
    " FIRST FINDS NODE N IN THE BST
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES OF A SUBTREE ARE TRAVERSED (POST ORDER)
    " THEREFORE CALCULATING THE DEPTH OF THE ROOT NODE
    " WRITTEN BY CHRIS HODDER
    """
    ##method for getting level of an arbitrary node
    def  getNodeDepthHelper(self, node,  depth,  key) :
            if node == None:
                return  0
            if key == node.element :
                return  depth
                #check left subtree for node
            found = self.getNodeDepthHelper(node.left, depth + 1, key)
            if found == 0:
              #check right subtree for node
                found = self.getNodeDepthHelper(node.right, depth + 1, key)
            return  found
    ##method for getting level of an specified node
    def getNodeDepth(self, key):
        if self.root == None:
            print("Empty Tree")
            return
        #find depth 
        found = self.getNodeDepthHelper(self.root, 1, key)
        if found != 0:
            print(f'Node {key}, is at depth : {found}')
        else :
            print(f'Node {key} not in tree')


    # Preorder traversal from the root
    def preorder(self):
      self.preorderHelper(self.root)

    # Preorder traversal from a subtree
    def preorderHelper(self, root):
      if root != None:
        print(root.element, end = " ")
        self.preorderHelper(root.left)
        self.preorderHelper(root.right)


    """
    " GET SUBTREE NODES
    " FIRST FINDS NODE N IN THE BST
    " THEN RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES OF N'S SUBTREE ARE TRAVERSED (PRE ORDER)
    " PRINTING EACH NODE AND RETURNING THE TOTAL NUMBER OF NODES
    " WRITTEN BY JACK ELLIS
    """
    def getSubtreeNodes(self, e):
        # first search for node e in the BST
        current = self.root
        while current != None:
            if e < current.element:
                current = current.left
            elif e > current.element:
                current = current.right
            else:
                # once node e is found
                # pass an empty list into the function
                # to append the subtree nodes to
                nodes = []
                nodes = self.getSubtreeNodeHelper(current, nodes)
                # return the total number of subtree nodes
                return nodes
        # if node e not found
        return None

    def getSubtreeNodeHelper(self, root, nodes):
        if root != None:
            nodes.append(root.element)
            self.getSubtreeNodeHelper(root.left, nodes)
            self.getSubtreeNodeHelper(root.right, nodes)
        return nodes
            

    # Return true if the tree is empty
    def isEmpty(self):
      return self.size == 0

    # Remove all elements from the tree
    def clear(self):
      self.root == None
      self.size == 0

    # Return the root of the tree
    def getRoot(self):
      return self.root


