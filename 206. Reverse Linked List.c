struct ListNode* reverseList(struct ListNode* head){
    struct ListNode* curr;
    struct ListNode* next;
    struct ListNode* prev;
    curr = head;
    prev = NULL;
    
    while (curr != NULL) {
        next = curr->next;
        curr->next = prev; 
        prev = curr;
        curr = next;
    }
    
    return prev;
}