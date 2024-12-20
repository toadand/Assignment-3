import bst              # BST class
import a3_io            # input/ output functions
import random           # to get random sample of integers

import bst_preprocess   # module to preprocess a list of integers
                        # for establishing a balanced BST on initial insertion

if __name__ == '__main__':

    TEST_CASE = [12, 45, 6, 8, 21, 34, 5, 55, 65, 543, 18, 90, 122, 132, 57, 66, 100]

    """ INITIALISE BST INTEGER VALUES """
    main_menu = {
            1: 'Pre-load a sequence of integers to build a BST',
            2: 'Manually enter integer values/keys, one by one, to build a BST',
            3: 'Exit'
            }

    while True:
        main_selection = a3_io.get_selection(main_menu)

        # 1) ENTER A SEQUENCE OF INTEGERS
        if main_selection == 1:
            while True:
                try:
                    integers = input('\nPlease enter a sequence of integers separated by commas\n(or [a]utogenerate/ [t]est case):\n> ').lower()
                    if integers == 'a':
                        integers = random.sample(range(1, 200), 20)
                        break
                    if integers == 't':
                        integers = TEST_CASE
                        break
                    integers = integers.replace(" ", "")
                    integers = integers.split(',')
                    for i, v in enumerate(integers):
                        integers[i] = int(v)
                    break
                except ValueError:
                    print('Please enter integer values only.')
            

        # 2) MANUALLY ENTER INTEGERS ONE-BY-ONE
        if main_selection == 2:
            print('')
            integers = []
            while True:
                new_int = a3_io.get_int('Please enter an integer to add to the BST (or 0 when finished): ', min_val = 0)
                if new_int == 0 and len(integers) != 0:
                    print('You have entered the integers:', a3_io.list_to_string(integers, ', '))
                    break
                if new_int == 0 and len(integers) == 0:
                    print('BST must have a minimum of 1 node.')
                    continue
                integers.append(new_int)

        # 3) EXIT
        if main_selection == 3:
            break


        """ PRE-PROCESS INTEGER LIST AND CREATE THE BST """

        # rearrange the list of integers so that
        # their sequential insertion into a BST
        # results in a balanced BST
        print('\nRearranging the list of integers...')
        print('Original integer values:', integers)  
        preprocessed_integers = bst_preprocess.preprocess(integers)
        print('Pre-processed integer values:', preprocessed_integers)

        # initialise a BST object and insert the pre-processed integers
        bst = bst.BinaryTree()
        for i in preprocessed_integers:
            bst.insert(i)


        """ INTERACT WITH BST """

        sub_menu = {
        1: 'Print the pre-order, in-order, and post-order traversal sequences of the BST',
        2: 'Print all leaf nodes of the BST, and all non-leaf nodes (separately)',
        3: 'Print the total number of nodes of a subtree',
        4: 'Print the depth of a node in the BST',
        5: 'Print the depth of a subtree rooted at a particular node',
        6: 'Insert a new integer key into the BST',
        7: 'Delete an integer key from the BST',
        8: 'Exit'
        }

        while True:
            print('\n')
            sub_selection = a3_io.get_selection(sub_menu)

            # 1) PRINT TRAVERSALS
            if sub_selection == 1:
                print('\nPre-order traversal:')
                bst.preorder()
                print('\nIn-order traversal:')
                bst.inorder()
                print('\nPost-order traversal:')
                bst.postorder()

            # 2) PRINT LEAF NODES AND NON-LEAF NODES
            if sub_selection == 2:
                print('\nLeaf nodes:')
                bst.printLeafNodes()
                print('\n\nNon-leaf nodes:')
                bst.printNonLeafNodes()

            # 3) PRINT TOTAL NUMBER OF NODES OF A subtree ROOTED AT A GIVEN NODE
            if sub_selection == 3:
                node = a3_io.get_int('Please enter a node to derive the nodes of its subtrees: ', min_val = 1)
                sub_nodes = bst.getSubtreeNodes(node)
                if sub_nodes == None: # if the node is not found in the BST
                    print(f'\nNode {node} not found.')
                else:
                    print(f'\nNodes of subtree rooted at {node}:\n{sub_nodes}')
                    print(f'\nTotal number of nodes of the subtree rooted at {node}: {len(sub_nodes)}')

            # 4) PRINT DEPTH OF A BST NODE
            if sub_selection == 4:
                node = a3_io.get_int('Please enter a node to derive its depth: ', min_val = 1)
                depth = bst.getNodeDepth(node)

            # 5) PRINT DEPTH OF A subtree ROOTED AT A GIVEN NODE
            if sub_selection == 5:
                node = a3_io.get_int('Please enter a node to derive the depth of its subtree: ', min_val = 1)
                sub_depth = bst.getSubtreeDepth(node)
                print(sub_depth)

            # 6) INSERT A NEW INTEGER
            if sub_selection == 6:
                new_int = a3_io.get_int('Please enter an integer to add to the BST: ', min_val = 1)
                bst.insert(new_int)

            # 7) DELETE AN INTEGER
            if sub_selection == 7:
                delete_key = a3_io.get_int('Please enter a key to delete: ')
                bst.delete(delete_key)

            # 8) EXIT
            if sub_selection == 8:
                break














            
