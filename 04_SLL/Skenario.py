
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

if __name__ == "__main__":
    linked_list = LinkedList()

    # Skenario 1: List masih kosong (head=NULL)
    print("Skenario 1: List masih kosong (head=None)")
    linked_list.display()

    # Skenario 2: Masukkan data baru (5) ke depan (head)
    print("\nSkenario 2: Masukkan data baru (5) ke depan (head)")
    linked_list.prepend(5)
    linked_list.display()

    # Skenario 3: Datang data baru (20) ke depan (head)
    print("\nSkenario 3: Datang data baru (20) ke depan (head)")
    linked_list.prepend(20)
    linked_list.display()