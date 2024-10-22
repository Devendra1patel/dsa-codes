#include <iostream>
using namespace std;
class Node
{
public:
    int data;
    Node *next;
    Node()
    {
        data = 0;
        next = NULL;
    }
};
class LinkedList
{
public:
    Node *head;
    LinkedList()
    {
        head = NULL;
    }
    void insertTail(int data)
    {
        Node *node ; 
        node = new Node();
        node->data = data ;
        if (  head == NULL)
        {
            head = node;
        }
        else
        {
            Node *tmp = head;
            while (tmp->next != NULL)
            {
                tmp = tmp->next;
            }
            tmp->next = node;
        }
    }
    void insertHead(int data)
    {
        Node *node = new Node();
        node->data = data;
        node->next = head;
        head = node;
    }
    int length()
    {
        Node *tmp;
        tmp = head;
        int count=0;
        while (tmp != NULL)
        {
            count++;
            tmp = tmp->next;
        }
        return count;
    }
    void deleteTail()
    {
        
        if (  head == NULL)
        {
            cout<<"Empty";
        }
        else if(head->next == NULL)
        {
            head = NULL;
        }
        else
        {
            Node *tmp = head;
            while (tmp->next->next != NULL)
            {
                tmp = tmp->next;
            }
            tmp->next = NULL;
        }
    }
    void deleteHead()
    {
        
        if (  head == NULL)
        {
            cout<<"Empty";
        }
        else 
        {
            head = head->next;
        }
    }

    void traverseList()
    {
        Node *tmp;
        tmp = head;
        while (tmp != NULL)
        {
            cout << "->" << tmp->data;
            tmp = tmp->next;
        }
    }
};
// Q1.----------------------------------------------------
// # Problem 1: Reverse a singly linked list.
// # Input: 1 -> 2 -> 3 -> 4 -> 5
// # Output: 5 -> 4 -> 3 -> 2 -> 1
void reverseList(Node*& head)
{
    Node *current = head;
    Node *prev, *tmp;
    if(head == NULL || head->next == NULL )
    {}
    else {
        prev = current->next;
        current->next = NULL ;
        while(prev->next)
        {
            tmp  = prev->next;
            prev->next = current;
            current = prev;
            prev = tmp;
        }
        prev->next = current;
        head = prev;
    }
}

// roblem 2: Merge two sorted linked lists into one sorted linked list.
// Input: List 1: 1 -> 3 -> 5, List 2: 2 -> 4 -> 6
// Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6
void mergeTwoSortedList(LinkedList& l1,LinkedList& l2)
{
    Node *i = l1.head, *iNext, *iPrev ;
    Node *j = l2.head, *jNext, *jPrev;
    while(j !=NULL || i!=NULL )
    {
        if(i->data < j->data)
        {
            iNext = i->next;
            i->next = j;
            i = i->next;
            i->next = iNext;
            j = j->next;
        }
        else{
            iPrev = j;
            // iPrev->next = 
        }
    }

}

// Problem 3: Remove the nth node from the end of a linked list.
// Input: 1 -> 2 -> 3 -> 4 -> 5, n = 2
// Output: 1 -> 2 -> 3 -> 5
void DeleteEndNode(LinkedList& l1)
{
    Node *tmp_head = l1.head;
    Node *head = tmp_head;
    if(head == NULL || head->next == NULL)
    {
        head = NULL;
    }   
    else{
    
        while(head->next->next != NULL)
        {
        // cout<<"hello";
            head  = head->next;
        }
        head->next = NULL;
    }
}
// -----------------------------------------------------------------------
// Problem 4: Find the intersection point of two linked lists.
// Input: List 1: 1 -> 2 -> 3 -> 4, List 2: 9 -> 8 -> 3 -> 4
// Output: Node with value 3
// -----------------------------------------------------------------------

// Problem 5: Remove duplicates from a sorted linked list.
// Input: 1 -> 1 -> 2 -> 3 -> 3
// Output: 1 -> 2 -> 3
void removeDuplicats(LinkedList& l1)
{
    Node *status, *current;
    status = l1.head;
    current = l1.head;
    
    if(status != NULL){
        while(current->next!=NULL){
            while(current->next != NULL && current->data == current->next->data)
            {
                current = current->next;
            }
            if(current->next != NULL)
            {
                current = current->next;
            status->next = current;
            status = status->next;
            }
        }
    }
}
// -------------------------------------------------------------------------
// Problem 6: Add two numbers represented by linked lists (where each node contains a single digit).
// Input: List 1: 2 -> 4 -> 3, List 2: 5 -> 6 -> 4 (represents 342 + 465)
// Output: 7 -> 0 -> 8 (represents 807)
int addDigits(Node* head, int num)
{
   if(head==NULL)
     return 0 ;
   num = addDigits(head->next,num);
   return num = num*10 + head->data; 
}
int addTwoList(LinkedList* l1, LinkedList* l2)
{
    int num1=0, num2=0;
    Node *head1 = l1->head ;
    Node *head2 = l2->head ;
    num1 = addDigits(head1, num1);
    num2 = addDigits(head2, num2);
    return num1+num2;
}
// ----------------------------------------------------------------
// Problem 7: Swap nodes in pairs in a linked list.
// Input: 1 -> 2 -> 3 -> 4
// Output: 2 -> 1 -> 4 -> 3
// ???????????????????????

Node* swapNode(LinkedList* l1)
{
    Node *headReal = l1->head;
    Node *head = headReal;
    Node *tmp, *prev=headReal;
    if(head!=NULL && head->next!=NULL)
    {
       headReal = headReal->next;
    }
    while(head!=NULL && head->next!=NULL )
    {
        tmp = head->next;
        head->next = tmp->next;
        tmp->next = head;
        // prev->next = tmp;
        // prev = head;
        // head = head->ne7xt;
    }
    return headReal;
} 
// ----------------------------------------
// Problem 8: Reverse nodes in a linked list in groups of k.
// Input: 1 -> 2 -> 3 -> 4 -> 5, k = 3
// Output: 3 -> 2 -> 1 -> 4 -> 5
Node* reverseKNode(LinkedList* l1, int k)
{
    Node *headReal = l1->head;
    Node *head = headReal, *prev = NULL, *tmp = NULL;
    int listSize = l1->length();
    if(listSize < k || headReal == NULL || head->next == NULL)
    {return headReal;}
    while(head!=NULL && k>0)
    {
        tmp = head->next;
        head->next = prev;
        prev = head;
        head = tmp;
        k--;
    }
    headReal->next = tmp;
    headReal = prev;
    return headReal;
}
// --------------try and solve tmprory not assigmen question----------------------
 Node* mergeTwoLists(LinkedList* l1, LinkedList* l2) {
        Node *head=NULL, *realHead=NULL;
        Node *list1 = l1->head, *list2 = l2->head;
        if(list1 != NULL && list2 != NULL)
        {
             if(list1->data < list2->data)
            {
                
                    head = list1;
                    list1 = list1->next;
                    realHead = head;
            }
            else{
                    head = list2;
                    list2 = list2->next;
                    realHead = head;
            }
        }
        else{
            if(list1 == NULL)
                return list1;
            else
                return list2;
        }
        while(list1 != NULL && list2 != NULL)
        {
            if(list1->data < list2->data)
            {
            // cout<<"test1- "<<list1->data<<" ";
                    head->next = list1;
                    list1 = list1->next;
                    head = head->next;
            }
            else if(list1->data == list2->data){
            // cout<<"test2- "<<list1->data<<" ";
                head->next = list1;
                head = head->next;
                head->next = list2;
                list1 = list1->next;
                list2 = list2->next;
            }
            else{
            cout<<"test3- "<<list2->data<<" ";
                    head->next = list2;
                    list2 = list2->next;
                    head = head->next;   
            }
        }
        if(list1 != NULL)
        {
            head->next = list1;
            // list1 = list1->next;
            // head = head->next;
        }
         if(list2 != NULL)
        {
            head->next = list2;
            // list2 = list2->next;
            // head = head->next;
        }
        // head->next = NULL;
        return realHead;
    }

int main()
{
    LinkedList l1,l2,l3;
    l1.insertTail(5);
    l1.insertTail(6);
    l1.insertTail(6);
    l1.insertTail(7);
    l1.insertTail(8);
    // l1.insertTail(8);
    // l1.insertTail(8);
    // l1.insertTail(9);
    // l1.insertTail(10);
    // l1.insertHead(12);
    l2.insertTail(1);
    l2.insertTail(2);
    l2.insertTail(4);
    l2.insertTail(4);
    l2.insertTail(7);
    l2.insertTail(8);
    l2.traverseList();
    cout<<"\n";
    cout<<"hello";
    l3.head = mergeTwoLists(&l1, &l2);
    l2.traverseList();
    // l2.head = reverseKNode(&l2, 3);
    // l2.head = swapNode(&l2); 
    // int num = addTwoList(&l2, &l1);
    // cout<<num;
    // l1.deleteTail();
    // removeDuplicats(l1);
    // reverseList(l1.head);
    // DeleteEndNode(l1);
    // l1.traverseList();
    // cout<<endl<<l1.length();
    return 0;
}


