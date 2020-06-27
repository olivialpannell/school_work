from sys import argv
from pQueue import pQueue

def main(argv):
    counter = 0
    file = open(argv[1], "r")
    for i in file:
        counter += 1

    p = pQueue(counter)
    file = open(argv[1], "r")
    for i in file:
        i = i.strip()
        cmd = i.split(' ')

        if cmd[0] == "print":
            p.printQueue()
        elif cmd[0] == "extractMax":
            print(p.extractMax())
        elif cmd[0] == "maximum":
            print(p.maximum())
        elif cmd[0] == "isEmpty":
            if p.isEmpty():
                print("Empty")
            else:
                print("Not Empty")
        elif cmd[0] == "insert":
            p.insert(int(cmd[1]))
        else:
            print("Command not found")

            

if __name__ == "__main__":
    main(argv)
