outputdebug = True 

def debug(msg):
    if outputdebug:
        print (msg)

class Node():
    def __init__(self, key):
        self.key = key
        self.left = None 
        self.right = None 



class AVLTree():
    def __init__(self, *args):
        self.node = None 
        self.height = -1  
        self.balance = 0; 
        
        if len(args) == 1: 
            for i in args[0]: 
                self.insert(i)
                
    def height(self):
        if self.node: 
            return self.node.height 
        else: 
            return 0 
    
    def is_leaf(self):
        return (self.height == 0) 
    
    def insert(self, key):
        tree = self.node
        
        newnode = Node(key)
        
        if tree == None:
            self.node = newnode 
            self.node.left = AVLTree() 
            self.node.right = AVLTree()
            debug("Inserted key [" + str(key) + "]")
        
        elif key < tree.key: 
            self.node.left.insert(key)
            
        elif key > tree.key: 
            self.node.right.insert(key)
        
        else: 
            debug("Key [" + str(key) + "] already in tree.")
            
        self.rebalance() 


    """
    " DELETE METHOD
    " 4 CASES TO CONSIDER WHEN DELETING NODE k:
    " 1) NODE HAS NO CHILDREN (IS A LEAF NODE) - SIMPLY DELETE NODE k
    " 2) NODE HAS 1 LEFT CHILD - REPLACE k WITH CHILD
    " 3) NODE HAS 1 RIGHT CHILD - REPLACE k WITH CHILD
    " 4) NODE HAS 2 CHILDREN - REPLACE k WITH IN-ORDER SUCCESSOR
    " WRITTEN BY JACK ELLIS
    """
    def delete(self, key):
        
        # print error message if traversed too far
        if self.node is None:
            debug("ERROR: Key [" + str(key) + "] not found.")
            return
        
        # if current node is the key to delete
        if self.node.key == key:
            # case 1 - node has no children
            # simply delete the node
            if self.is_leaf():
                print(f'{self.node.key} has no children and is simply deleted.')
                self.node = None 
            # case 2 - node has 1 child (right)
            elif self.node.left.node is None:
                print(f'{self.node.key} has 1 right child.')
                print(f'Replacing {self.node.key} with right child {self.node.right.node.key}')
                child = self.node.right.node
                print('Deleting original child node...')
                self.node.right.delete(child.key)
                self.node.key = child.key
            # case 3 - node has 1 child (left)
            elif self.node.right.node is None:
                print(f'{self.node.key} has 1 left child.')
                print(f'Replacing {self.node.key} with left child {self.node.left.node.key}')
                child = self.node.left.node
                print('Deleting original child node...')
                self.node.left.delete(child.key)
                self.node.key = child.key
            # case 4 - node has 2 children
            # copy successor to the current node
            elif self.node.left.node is not None and self.node.right.node is not None:
                print(f'{self.node.key} has 2 children.')
                successor = self.logical_successor(self.node)
                new_key = successor.key # set the key in case it's overriden by recursive function call
                print(f'Replacing {self.node.key} with successor {successor.key}')
                print('Deleting original successor node...')
                self.node.right.delete(successor.key)
                self.node.key = new_key

        # else recursively call the function until the node is found
        elif key < self.node.key: 
            self.node.left.delete(key)
        else: 
            self.node.right.delete(key)

        # rebalance after deletion
        self.rebalance()
        

    def rebalance(self):
        ''' 
        Rebalance a particular (sub)tree
        ''' 
        # key inserted. Let's check if we're balanced
        self.update_heights(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.node.left.balance < 0:  
                    self.node.left.lrotate() # we're in case II
                    self.update_heights()
                    self.update_balances()
                self.rrotate()
                self.update_heights()
                self.update_balances()
                
            if self.balance < -1:
                if self.node.right.balance > 0:  
                    self.node.right.rrotate() # we're in case III
                    self.update_heights()
                    self.update_balances()
                self.lrotate()
                self.update_heights()
                self.update_balances()
            
    def rrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' right') 
        A = self.node 
        B = self.node.left.node 
        T = B.right.node 
        
        self.node = B 
        B.right.node = A 
        A.left.node = T 
    
    def lrotate(self):
        # Rotate left pivoting on self
        debug ('Rotating ' + str(self.node.key) + ' left') 
        A = self.node 
        B = self.node.right.node 
        T = B.left.node 
        
        self.node = B 
        B.left.node = A 
        A.right.node = T 
            
    def update_heights(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_heights()
                if self.node.right != None:
                    self.node.right.update_heights()
            
            self.height = max(self.node.left.height,
                              self.node.right.height) + 1 
        else: 
            self.height = -1 
            
    def update_balances(self, recurse=True):
        if not self.node == None: 
            if recurse: 
                if self.node.left != None: 
                    self.node.left.update_balances()
                if self.node.right != None:
                    self.node.right.update_balances()

            self.balance = self.node.left.height - self.node.right.height 
        else: 
            self.balance = 0 

    def logical_predecessor(self, node):
        ''' 
        Find the biggest valued node in LEFT child
        ''' 
        node = node.left.node 
        if node != None: 
            while node.right != None:
                if node.right.node == None: 
                    return node 
                else: 
                    node = node.right.node  
        return node 
    
    def logical_successor(self, node):
        ''' 
        Find the smallest valued node in RIGHT child
        ''' 
        node = node.right.node  
        if node != None: # just a sanity check  
            
            while node.left != None:
                debug("LS: traversing: " + str(node.key))
                if node.left.node == None: 
                    return node 
                else: 
                    node = node.left.node  
        return node 

    def check_balanced(self):
        if self == None or self.node == None: 
            return True
        
        # We always need to make sure we are balanced 
        self.update_heights()
        self.update_balances()
        return ((abs(self.balance) < 2) and self.node.left.check_balanced() and self.node.right.check_balanced())  

        
    """
    " PRE-ORDER TRAVERSAL METHOD
    " WRITTEN BY JACK ELLIS
    """
    def preorder_traverse(self):
        if self.node == None:
            return []
        inlist = []
        # root
        inlist.append(self.node.key)
        # left
        l = self.node.left.preorder_traverse()
        for i in l: 
            inlist.append(i) 
        # right
        r = self.node.right.preorder_traverse()
        for i in r: 
            inlist.append(i) 
        return inlist


    def inorder_traverse(self):
        if self.node == None:
            return [] 
        inlist = []
        # left
        l = self.node.left.inorder_traverse()
        for i in l: 
            inlist.append(i) 
        # root
        inlist.append(self.node.key)
        # right
        r = self.node.right.inorder_traverse()
        for i in r: 
            inlist.append(i) 
        return inlist 


    """
    " POST-ORDER TRAVERSAL METHOD
    " WRITTEN BY JACK ELLIS
    """
    def postorder_traverse(self):
        if self.node == None:
            return []
        inlist = []
        # left
        l = self.node.left.postorder_traverse()
        for i in l: 
            inlist.append(i) 
        # right
        r = self.node.right.postorder_traverse()
        for i in r: 
            inlist.append(i)
        # root
        inlist.append(self.node.key)
        return inlist 


    def display(self, level=0, pref=''):
        '''
        Display the whole tree (but turned 90 degrees counter-clockwisely). Uses recursive def.
        '''        
        self.update_heights()  # Must update heights before balances 
        self.update_balances()  
        if(self.node != None): 
            print ('-' * level * 2, pref, self.node.key, "[" + str(self.height) + ":" + str(self.balance) + "]", 'L' if self.is_leaf() else ' ')    
            if self.node.left != None: 
                self.node.left.display(level + 1, '<')
            if self.node.left != None:
                self.node.right.display(level + 1, '>')


    """
    " PRINT LEAF NODES METHOD
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES ARE TRAVERSED (IN ORDER)
    " AND ALL LEAF NODES ARE PRINTED
    " WRITTEN BY JACK ELLIS
    """
    def print_leaf_nodes(self):
        if self.node != None:
            if self.node.left != None:
                self.node.left.print_leaf_nodes()
            if self.is_leaf():
                print(self.node.key, end = " ")
            if self.node.right != None:
                self.node.right.print_leaf_nodes()


    """
    " PRINT NON LEAF NODES METHOD
    " RECURSIVELY CALLS THE FUNCTION UNTIL ALL NODES ARE TRAVERSED (IN ORDER)
    " AND ALL NON LEAF NODES ARE PRINTED
    " WRITTEN BY JACK ELLIS
    """
    def print_nonleaf_nodes(self):
        if self.node != None:
            if self.node.left != None:
                self.node.left.print_nonleaf_nodes()
            if not self.is_leaf():
                print(self.node.key, end = " ")
            if self.node.right != None:
                self.node.right.print_nonleaf_nodes()
