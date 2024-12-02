/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* reverseList(ListNode* head) {

    ListNode* ptr = head;
    ListNode* F = head;    
    int co = 0;
    while(ptr != nullptr){
        ptr = ptr->next;
        co++;
    }
    ptr = F;
    int a[100000];

    for(int i = 0;i<co;i++){
        a[i] = ptr->val;
        ptr = ptr->next;
    }
    ptr = F;
    for(int i = co-1;i>=0;i--){
        ptr->val = a[i] ;
        ptr = ptr->next;
    }

    ptr = F;
    return ptr;
    }
};