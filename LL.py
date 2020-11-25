class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LL:
    def __init__(self):
        self.head = None
        self.tail = None

    def getLast(self):
        curr = self.head
        while curr.next != None:
            curr = curr.next
        return curr

    def traverse(self):
        count = 0
        curr = self.head
        while curr != None and count <50:
            print("-", curr.data, end=" ")
            curr = curr.next
            count += 1
        print()

    def push(self, data):
        new = Node(data)
        last = self.getLast()
        last.next = new

    def insertHead(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def findMiddle(self):
        fast, slow = self.head, self.head
        dat = 0
        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            dat = slow.data
        print("middle element is", dat)

    def findMid(self):
        count = 0
        fast, slow = self.head, self.head
        while fast.next != None:
            if count %2 == 0:
                slow = slow.next
            fast = fast.next
            count += 1
        print("mid el", slow.data)


    def findQuarter(self):
        fast, slow = self.head, self.head
        dat = 0
        while fast and fast.next and fast.next.next != None:
            fast = fast.next.next.next
            slow = slow.next
            dat = slow.data

        print("Quarter element is", dat)

    def findLoop(self):
        fast, slow = self.head, self.head
        while slow and fast!= None and fast.next != None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                print("Loop found at", slow.data)
                break
    


if __name__ == "__main__":
    ll = LL()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    one.next = two
    two.next = three
    ll.head = one

    ll.push(4)
    ll.insertHead(0)
    ll.push(5)
    ll.push(6)
    ## create a loop
    # last = ll.getLast()
    # last.next = two

    # ll.findLoop()

    ll.findMiddle()
    ll.findQuarter()
    ll.findMid()
    ll.traverse()