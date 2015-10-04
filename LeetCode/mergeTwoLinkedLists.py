
def mergeTwoLists(self, l1, l2):
    head = ListNode(0)
    current = ListNode(0)
    
    #set head as current
    current = head
    
    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 =  l2.next
        current = current.next 
    current.next = l1 or l2
    return head.next 
