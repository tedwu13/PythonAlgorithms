def addLinkedListsReverse(l1, l2):
    if l1 == None or l2 == None:
        return 0

    while l1.next != None or l2.next != None or carry != None:
        digitSum = carry
        if l1 != None:
            digitSum += l1.val
            l1 = l1.next
        if l2 != None:
            digitSum += l2.val
            l2 = l2.next
        l3.val = digitSum % 10
        l3.next = l3

        carry = digitSum / 10
    return l3

