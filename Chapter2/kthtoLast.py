def kthtoLast(head, k):
    if k <= 0: 
        print "invalid k"
    pointer1 = head
    pointer2 = head

#it is k-1 and not k

    for i in range(k-1):
        if pointer2 == None:
            return None
        pointer2 = pointer2.next

    while pointer2.next != None:
        pointer1 = pointer1.next
        pointer2 = pointer2.next
    return pointer1

    