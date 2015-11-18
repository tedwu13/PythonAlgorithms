class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addNode(self, data):

    def removeNode(self, data):

    def printLinkedList(self):


def printRemovedNode(head, value):
    if head.val == value:
        return head.next 
    while head.next.val != None:
        if head.next.val == value:
            temp = head.next
            head.next = head.next.next
            return temp
        else:
            temp = temp.next


def getRandomNode(head):
    k = 2
    returned = head

    while head != None:
        if randomProbability(k):
            returned = head
        else:
            head = head.next
            k = k + 1
    return returned


def randomProbability(k):
    #return true if it is probablity 1/k
    random = random.randInt(0,k-1)
    if random % k == 0:
        return True

