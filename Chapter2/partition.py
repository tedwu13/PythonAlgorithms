def partition(head, x):
    start = head
    end = head

    while head != None:
        if head.val < x:
            head.next = start
            start = head
        else:
            end.next = head
            end = head
        head = head.next
    end.next = None
    return head


    

