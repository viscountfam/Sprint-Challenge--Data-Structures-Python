class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
            # Case 1: value is less than self.value
        if value < self.value:

            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)

            # Else ??????
            else:
                # repeat the process on the left subtree
                self.left.insert(value)


        # Case 2: value is greater or equal to than self.value
        elif value >= self.value:

            if self.right is None:
                self.right = BSTNode(value)

            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop most likely the while loop
        current = self
        next_node = current.right

        while next_node is not None:
            current = next_node
            next_node = self.right.right
        
        return current.value
        # maximum = 0
        # current = self
        # while current is not None:
        #     if current.value > maximum:
        #         maximum = current.value
        #     current = current.right
        # return maximum
    # def recursive_getmax(self):
    #     if self.right is None:
    #         return self.value
    #     return self.right.recursive_getmax()
    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # we need a function to handle the right using a loop
        # we need an identical function to handle it for the left
        # we need these functions to be called recursively
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # traversal = ""
        # if self:
        #     traversal = self.in_order_dft(self.left)
        #     traversal += (str(node.value) + ",")
        #     traversal = self.in_order_dft(self.right)
        # return traversal
        if self is None:
            return 
        # check if we can "move left"
        if self.left:
            self.left.in_order_print()
        
        # visit the node by printing its value
        print(self.value)

        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print()

        



    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # Use a queue to form a line
        # for the nodes to "get in"
        newqueue = Queue()
        
        # start by placing the root in the queue
        newqueue.enqueue(self)
        # need a while loop to iterate
        while len(newqueue > 0):
        # while length of queue is greater than 0
            # dequeue item from front of queue
            # print that item
            print(self.value)
            node = newqueue.dequeue()
        # place current item's left node in queue if not None
        if node.left:
            newqueue.enqueue(node.left)
        # place current item's right node in queue if not None
        if node.right:
            newqueue.enqueue(node.right)
    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initalize an empty stack
        stack = Stack()

        # add your root to the stack
        stack.push(self)

        #create a while loop to manage our iteration
        # if stack is not empty enter the while loop
        while len(stack) > 0:
            #pop top item off the stack
            node = stack.pop()
            # print that item's value
            print(node.value)
        # if there is a right subtree
        if node.right:
            # push right item onto the stack
            stack.push(node.right)
        # push the right item on first because a stack is first in first out
        # if there is a left subtree
        if node.left:
            # push left item onto the stack
            stack.push(node.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        # traversal = ""
        # if node:
        #     traversal += (str(node.value) + ",")
        #     traversal = self.pre_order_dft(node.left, traversal)
        #     traversal = self.pre_order_dft(node.right, traversal)
        # return traversal
        
        if self is None:
            return

        print(self.value)

        if self.left is not None:
            self.left.pre_order_dft()

        if self.right is not None:
            self.right.pre_order_dft()





    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        # traversal = ""
        # if node:
        #     traversal = self.pre_order_dft(node.left, traversal)
        #     traversal = self.pre_order_dft(node.right, traversal)
        #     traversal += (str(node.value) + ",")
        # return traversal
        if self is None: 
            return
        
        if self.left is not None:
            self.left.post_order_dft()

        if self.right is not None:
            self.right.post_order_dft()

        print(self.value)
