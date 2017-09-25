





class Node:
    value = None
    parent = None
    left = None
    right = None

    def __init__(self,val):
        self.value = val

    def getvalue(self):
        return self.value

    def getparent(self):
        return self.parent

    def getleft(self):
        return self.left

    def getright(self):
        return self.right



class BST():



    root = None

    def __init__(self,A):

        self.root = Node(A[0])

        for value in A[1:]:

            self.insert(value)

    def insert(self,value):

        currentNode = self.root

        newnode = Node(value)


        while (newnode.parent == None):

            # right node, parent right NIL
            if value >= currentNode.getvalue() and currentNode.getright() == None:

                currentNode.right = newnode
                newnode.parent = currentNode
                currentNode = self.root
            # left node, parent left NIL
            elif value <= currentNode.getvalue() and currentNode.getleft() == None:
                currentNode.left = newnode
                newnode.parent = currentNode
                currentNode = self.root

                # navigate into right node, start new iteration
            elif value >= currentNode.getvalue():
                currentNode = currentNode.right

                # navigate into left node, start new iteration
            else:
                currentNode = currentNode.left

    def inordertraversal(self):

        inorder(self.root)



    def find_min(self):

        currentnode = self.root

        while(currentnode.left != None):
            currentnode = currentnode.left



    def search(self,value):

        currentnode = self.root



        while(currentnode.left != None or currentnode.right != None):

            if currentnode.value == value:
                return currentnode
            if currentnode.value > value:
                currentnode = currentnode.left

            else:
                currentnode = currentnode.right


        if currentnode.value == value:
            return currentnode
        else:
            return None


    def find_larger(self,value):
        currentnode = self.root

        found = False

        while(not found): ## finds value in tree, moves on to next routine

            if currentnode.value == value:
                found = True

            elif(currentnode.value > value):
        # currentnode's value is larger than value that is searching for,
        # traversing to left node, if it exists. if it does not exist, that is where the value would be.
        # since it would be in the left node, the parentnode is the immediate next larger, so we return parentnode.

                if(currentnode.left != None):  # currentnode.left exists, traversing there
                    currentnode = currentnode.left
                else: # currentnode.left does not exist / searched value not in tree, returning parentnode( currentnode )
                    return currentnode
            else: # value is larger than currentnode, and traverses to right child.

                if(currentnode.right != None): # currentnode.right exists, traversing there
                    currentnode = currentnode.right





        if (currentnode.value == value): # current node is the node with the value.

            if(currentnode.right != None): # immediate larger exists for value, in the right subtree's minimum.
                currentnode = currentnode.right

                while(currentnode.left != None):
                    currentnode = currentnode.left

                return currentnode   ## find larger in immediate right subtree

                # next-larger node exists in next parentnode that has the currentnode as left child
                # OR next-larger does not exist and will return None


            while 1:
                if (currentnode.parent.left == currentnode):
                    return currentnode.parent

                    # returns None because there is no next-larger
                if (currentnode.parent == None):
                    return None
                else:
                    currentnode = currentnode.parent

















def inorder(node):

    if(node.left == None and node.right == None):
        pass
    elif node.left != None:
        inorder(node.left)


    print(node.value)

    if node.right != None:
        inorder(node.right)


    return




# A = [1,2,9,5,10,4,3,7,6,8]


A = [4, 1000, 48, 0, 13, 3, 7, 9, 666, 79, 4, 41, 5]









