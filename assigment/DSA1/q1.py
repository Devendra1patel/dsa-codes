# Problem 1: Reverse a singly linked list.
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1
class Node:
    def __init__(self):
        self.next = None
        self.data = None
    def setData(self,data):
        self.data = data
    def get(self):
        return self.data
    def setNext(self,next):
        self.next = next
    def getNext(self):
        return self.next

def createlinkedList(n):
    node = Node()
    tmp = node
    d  = input("Enter value:- ")
    tmp.setData(n)
    for i in range(0,n):
        d  = input("Enter value:- ")
        tmp_node = Node()
        tmp_node.setData(d)
        tmp.setNext(tmp_node)
        tmp = tmp_node
    return node
def traversevalues(node):
    tmp = node
    size = 0
    while(tmp is not None):
        t = tmp.get() 
        print("->",t,end="")
        tmp = tmp.getNext()
    
    
node1 =  createlinkedList(3)
traversevalues(node1)
# print(node1.getNext())
# -------------------------------------------------------------------------------------------
# Problem 1: Reverse a singly linked list.
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1
def size(node):
    t = node
    tmp = node
    len = 0
    while(tmp is not None):
        len+=1
        tmp = tmp.getNext()
