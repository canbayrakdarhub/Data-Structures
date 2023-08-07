class Node:
    #An object for storing a single node of a linked list.
    #Models two attributes : data and the link to the next node in the list.
    data = None
    next_node = None

    def __init__(self,data):
        self.data=data
    def __repr__(self):
        return "<Node data: %s>" %self.data





N1 = Node(10)
N2= Node(20)

N1.next_node = N2
print(N1)
print(N2)
print(N1.next_node)


class Linked_List:

    #singly Linked List

    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):

        #Return the number of nodes in the list Takes O(n) time
        current = self.head
        counter = 0

        while current != None:
            counter = counter + 1
            current = current.next_node

        return counter


    def add(self,data):

        #Adds a new node containing data at the head of the list.
        #Takes O(1) time

        new_node= Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self,key):

        #Search for the first node containing data that matches the key
        #O(n) Time
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None

    def insert(self,data,index):
        #Inserts a new Node containing data at index position
        #Insertion takes O(1) time but finding the node at the insertion point takes O(n)
        if index == 0:
            self.add(data)

        if index>1:
            new = Node(data)

            position = index
            current = self.head

            while position > 1:
                current = node.next_node
                position = position - 1
            prev_node = current
            next_node = current.next_node

            prev_node.next_node = new
            new.next_node = next_node

    def remove(self,key):

        #Removes node containing data that matches the key.
        #Returns the node or none if the key doesn't exist. O(n)time

        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node

            elif current.data == key:
                found = True
                previous.next_node = current.next_node

            else:
                previous = current
                current = current.next_node
        return current


    def __repr__(self):
        nodes = []
        current = self.head

        while current != None:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)

            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)

            current = current.next_node
        return ' -> '.join(nodes)


linked_list = Linked_List()
N1 = Node(10)
linked_list.head = N1
print(linked_list.size())


linked_list2 = Linked_List()
linked_list2.add(10)
print(linked_list2.size())

linked_list2.add(20)
linked_list2.add(30)

print(linked_list2.size())


list = Linked_List()
list.add(1)
list.add(2)
list.add(3)

print(list)

list1 = Linked_List()
list1.add(1)
list1.add(2)
list1.add(3)
list1.add(40)
n = list1.search(3)
print(n)


