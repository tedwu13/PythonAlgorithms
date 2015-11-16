def findBeginning(head):
    current = head
    runner = head
`
    while runner != None or runner.next != None:
        current = current.next
        runner = runner.next.next

        if runner == current:
            break

    if runner == None or runner.next == None:
        return None

    runner = head
    while runner != current:
        current = current.next
        runner = runner.next
    return runner

