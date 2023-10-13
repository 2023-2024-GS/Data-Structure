class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Membuat objek single linked list
sll = SingleLinkedList()

# Menambahkan data dari belakang
sll.append(10)
sll.append(15)
sll.append(21)

# Menampilkan data dalam single linked list
print("Data dalam single linked list:")
sll.display()
