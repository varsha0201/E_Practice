class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''

        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.next

        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_value(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count =0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next

        return count

    def remove_at(self, index):
        if index < 0 or index>self.get_lenght():
            raise Exception("Invalid index")

        if index == 0:
            self.head = self.head.next
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index>self.get_lenght():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_begining(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node(data, itr.next)
                itr.next = node
                break
           
            itr = itr.next
            count += 1

 


if __name__  == "__main__":
    ll = LinkedList()
    ll.insert_value([10,20,30,40,50,60])
    ll.insert_at_begining(111)
    # ll.insert_value(["banana", "mango","grapes", "orange","asd","qwe"])
    # ll.get_lenght()
    # ll.remove_at(30)
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(35)
    # ll.insert_at_end(89)
    # ll.insert_at_end(6)
    # ll.insert_at_end(52452)
    # ll.insert_at(0,"figs")
    # ll.insert_at(2,"Jackfruit")
    # ll.insert_at(4,"Test")
    ll.print()
    print("lenght:",ll.get_lenght())






















































































































































































































































































































































































































































































