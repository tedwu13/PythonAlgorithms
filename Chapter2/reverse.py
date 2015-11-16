def reverse(n):
    last = None
    current = n
    while(current is not None):
    nxt = current.nxt
    current.nxt = last
    last = current
    current = nxt
    return last

#reverse a linked list


