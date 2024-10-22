# singly linked list // 10/22/2024




        
class LinkedList:
    length = 0
    def __init__(self, data=None,  next=None):
        self.data = data
        self.next = next
    def setdata(self, data):
        self.data = data
    def getdata(self):
        return self.data
    def getnextnode(self):
        return self.next
    def setnextnode(self, next):
        self.next = next


head = LinkedList(10)
head1 = LinkedList(20)
head.setnextnode(head1)
head2 =  LinkedList(30)
head1.setnextnode(head2)


# print(head2.getdata())
# print(head.getdata())        

def traverse(head):
    current = head
    print("hello", head.getnextnode())
    while current.getnextnode() != None:
        print(current.getdata())
        current = current.getnextnode()
    print(current.getdata())
    
def traverse_recursivly(head):
    if head == None:
        return
    print(head.getdata(),"-> ",end='')
    return  traverse_recursivly(head.getnextnode())

def cal_len(head,  length=0):
   
    if head == None:
        return length
    length += 1
    return  cal_len(head.getnextnode(), length)
    
# print(cal_len(head))    
# traverse(head)
traverse_recursivly(head)
print("------")

def insert_node(head,data,k):
    len = cal_len(head)
    if(  k > len+1):
        print("k is not valid to insert head")
        return head
    if k == 1:
        return LinkedList(data,head)
    current = head
    while k > 2:
        current =  current.getnextnode()
        k -= 1
        
    new =  LinkedList(data, current.getnextnode())
    current.setnextnode(new) 
    return head

head = insert_node(head, 15, 5)
print(head.getdata())
traverse_recursivly(head)

    