# SSL dengan HEAD (Penambahan data dari depan)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Membuat objek single linked list
sll = SingleLinkedList()

# Menambahkan data dari depan
sll.prepend(10)
sll.prepend(15)
sll.prepend(10)

# Menampilkan data dalam single linked list
print("Data dalam single linked list:")
sll.display()