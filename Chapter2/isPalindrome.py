def isPalindrome(head):
    if head == None:
        return True

    fast = head
    slow = head

    stack = []
    while fast != None and fast.next != None:
        stack.append(slow.val)
        fast = fast.next.next
        slow = slow.next

    # has odd number of elements
    if fast != None:
        slow = slow.next

    while slow != None:
        if stack.pop() != slow.data:
            return False
        slow = slow.next

    return True
    