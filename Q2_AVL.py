import avl      # AVL tree class
import a3_io    # input/ output functions
import random   # to get random sample of integers

if __name__ == '__main__':

    TEST_CASE = [55, 81, 65, 20, 35, 79, 23, 14, 21, 103, 92, 45, 85, 51, 47, 48, 50, 46]

    """ INITIALISE AVL TREE INTEGER VALUES """
    main_menu = {
            1: 'Pre-load a sequence of integers to build an AVL tree',
            2: 'Manually enter integer values/keys, one by one, to build an AVL tree',
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
                new_int = a3_io.get_int('Please enter an integer to add to the AVL tree (or 0 when finished): ', min_val = 0)
                if new_int == 0 and len(integers) != 0:
                    print('You have entered the integers:', a3_io.list_to_string(integers, ', '))
                    break
                if new_int == 0 and len(integers) == 0:
                    print('AVL tree must have a minimum of 1 node.')
                    continue
                integers.append(new_int)

        # 3) EXIT
        if main_selection == 3:
            break


        """ INTERACT WITH AVL TREE """

        # initialise an AVL tree object with the list of integer values
        print('\nCreating the AVL tree...')
        avl_tree = avl.AVLTree(integers)

        sub_menu = {
        1: 'Display the AVL tree, showing the height and balance factor for each node.',
        2: 'Print the pre-order, in-order, and post-order traversal sequences of the AVL tree',
        3: 'Print all leaf nodes of the AVL tree, and all non-leaf nodes (separately)',
        4: 'Insert a new integer key into the AVL tree',
        5: 'Delete an integer key from the AVL tree',
        6: 'Exit'
        }

        while True:
            print('\n')
            sub_selection = a3_io.get_selection(sub_menu)

            # 1) DISPLAY AVL TREE
            if sub_selection == 1:
                avl_tree.display()

            # 2) PRINT TRAVERSALS
            if sub_selection == 2:
                print('\nPre-order traversal:\n', avl_tree.preorder_traverse())
                print('\nIn-order traversal:\n', avl_tree.inorder_traverse())
                print('\nPost-order traversal:\n', avl_tree.postorder_traverse())

            # 3) PRINT LEAF NODES AND NON-LEAF NODES
            if sub_selection == 3:
                print('\nLeaf nodes:')
                avl_tree.print_leaf_nodes()
                print('\n\nNon-leaf nodes:')
                avl_tree.print_nonleaf_nodes()

            # 4) INSERT A NEW INTEGER
            if sub_selection == 4:
                new_int = a3_io.get_int('Please enter an integer to add to the AVL tree: ', min_val = 1)
                avl_tree.insert(new_int)

            # 5) DELETE AN INTEGER
            if sub_selection == 5:
                delete_key = a3_io.get_int('Please enter a key to delete: ')
                avl_tree.delete(delete_key)

            # 6) EXIT
            if sub_selection == 6:
                break

