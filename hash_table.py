class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __str__(self):
        return f"{self.name}: {self.number}"


class Node:
    def __init__(self, key, value):
        self.key = key        
        self.value = value    
        self.next = None      


class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [None] * size

    def hash_function(self, key):
        return sum(ord(ch) for ch in key) % self.size

    def insert(self, key, value):
        """key = contact name, value = phone number string."""
        index = self.hash_function(key)
        current = self.data[index]

        while current:
            if current.key == key:
                current.value.number = value
                return
            current = current.next

        
        new_node = Node(key, Contact(key, value))
        if self.data[index] is None:
            self.data[index] = new_node
        else:
            current = self.data[index]
            while current.next:
                current = current.next
            current.next = new_node

    def search(self, key):
        current = self.data[self.hash_function(key)]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        return None

    def print_table(self):
        for i, head in enumerate(self.data):
            if head is None:
                print(f"Index {i}: Empty")
            else:
                parts = []
                current = head
                while current:
                    parts.append(f"- {current.value}")
                    current = current.next
                print(f"Index {i}: " + " ".join(parts))


if __name__ == "__main__":
    table = HashTable(10)
    table.print_table()

    table.insert("John", "909-876-1234")
    table.insert("Rebecca", "111-555-0002")
    table.print_table()

    print("\nSearch result:", table.search("John"))


    table.insert("Amy", "111-222-3333")
    table.insert("May", "222-333-1111")
    table.print_table()


    table.insert("Rebecca", "999-444-9999")
    table.print_table()

    # Edge Case #3 - Missing key
    print(table.search("Chris"))  