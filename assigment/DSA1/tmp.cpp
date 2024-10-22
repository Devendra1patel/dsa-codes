#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;


//  Definition for singly-linked list.
 struct ListNode {
     int val;
     ListNode *next;
     ListNode() : val(0), next(nullptr) {}
     ListNode(int x) : val(x), next(nullptr) {}
     ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
 
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int result;
        vector<double> l11;
        vector<double> l22;
        while (l1 != NULL) {
            l11.push_back(l1->val);
            l1 = l1->next;
        }
        while (l2 != NULL) {
            l22.push_back(l2->val);
            l2 = l2->next;
        }
        reverse(l11.begin(), l11.end());
        reverse(l22.begin(), l22.end());
        int sum_l1 = 0, sum_l2 = 0;
        for (int element : l11) {
            sum_l1 = sum_l1 * 10 + element;
        }
        for (int element : l22) {
            sum_l2 = sum_l2 * 10 + element;
        }
        result = sum_l1 + sum_l2;
        ListNode* res = nullptr;
        ListNode* tail = nullptr; // Keep track of the tail of the result list

        if(result == 0)
        {
            ListNode* newNode = new ListNode(0);
            return newNode;
        }
        while (result != 0) {
            int digit = result % 10;
            ListNode* newNode = new ListNode(digit);

            if (res == nullptr) {
                res = newNode;
                tail = res;
            } else {
                tail->next = newNode;
                tail = newNode; // Update the tail
            }
            result = result / 10;
        }
        return res;
    }
};
int main()
{
    Solution s1;
    ListNode *l1, *l2;
    l1
    cout<<s1.addTwoNumbers();
    return 0;
}