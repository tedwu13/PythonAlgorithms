def deleteDuplicates(self, head):
        if head == None or head.next == None:
            return head
        current = head
        
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next 
        return head
        