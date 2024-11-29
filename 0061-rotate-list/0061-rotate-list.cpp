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
    ListNode* rotateRight(ListNode* head, int k) {

        ListNode* temp = head;
        int c = 1;
        if (head == nullptr){
            return 0;
        }
        while(temp->next != nullptr){
            temp = temp->next;
            c ++;

        }
        temp->next = head;
        int l = c - k%c;
        for(int i = 0;i<l;i++){
             
            cout<<temp->val<<endl;
            temp = temp->next;
        }
        head = temp;
        head = head->next;
        temp->next = nullptr;

        

        
        return head;
    }
};