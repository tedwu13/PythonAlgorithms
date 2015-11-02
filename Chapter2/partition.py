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

linked list 

1->22->33->14->5->6
x = 6
1->5->6->14->22->33








