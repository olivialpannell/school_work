# Olivia Pannell
# HI i know I'm a few minutes late, please have mercy :(
from sys import argv
from BST import BST

def main(argv):
    #create a new tree
    tree = BST()



    #open file argument
    file = open(argv[1], "r")
    # goes for amount of of lines in f
    for line in file:
        text = line.split()
        #test cases for what the first element in the list is
        if text[0] == "insert":
            #saves the second element, since it exists
            data = text[1]
            tree.insert(data)
        elif text[0] == "delete":
            #saves element, then calls delete
            data = text[1]
            tree.delete(data)
        elif text[0] == "preorder" or text[0] == "postorder" or text[0] == "inorder":
            #tests for if a traverse then calls the function
            tree.traverse(text[0], tree.getRoot())
        else:
            print("incorrect format")

    return 0

if __name__ == "__main__":
    main(argv)
