class item:
    def __init__(self, i, n, d, p):
        self.id = i
        self.name = n
        self.desc = d
        self.price = p
        
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Desc: {self.desc}, Price: ${self.price:.2f}"


class manager:
    def __init__(self):
        self.items = []

    def create(self):
        try:
            i = int(input("Enter ID: "))
            if any(item.id == i for item in self.items):
                print("Error: ID exists.")
                return

            n = input("Enter name: ").strip()
            if not n:
                print("Error: Name required.")
                return

            d = input("Enter desc: ").strip()
            if not d:
                print("Error: Desc required.")
                return

            p = float(input("Enter price: "))
            if p < 0:
                print("Error: Invalid price.")
                return
            new_item = item(i, n, d, p)
            self.items.append(new_item)
            print("Item added.")
        except ValueError:
            print("Error: Invalid input.")

    def read(self):
        if not self.items:
            print("No items.")
            return
        print("\n===Items===")
        for item in self.items:
            print(item)
        print("============")

    def update(self):
        try:
            i = int(input("Enter ID to update: "))
            item = next((item for item in self.items if item.id == i), None)

            if not item:
                print("Error: Item not found.")
                return
            print("Current item:")
            print(item)

            n = input("Enter new name (leave blank to keep): ").strip()
            if n:
                item.name = n

            d = input("Enter new desc (leave blank to keep): ").strip()
            if d:
                item.desc = d

            p = input("Enter new price (leave blank to keep): ").strip()
            if p:
                item.price = float(p)
                if item.price < 0:
                    print("Error: Invalid price.")
                    return
            print("Item updated.")
        except ValueError:
            print("Error: Invalid input.")
    def delete(self):
        try:
            i = int(input("Enter ID to delete: "))
            item = next((item for item in self.items if item.id == i), None)

            if not item:
                print("Error: Item not found.")
                return
            self.items.remove(item)
            print("Item deleted.")
        except ValueError:
            print("Error: Invalid input.")

def menu():
    m = manager()
    while True:
        print("\n+-Item Manager-+")
        print("[C] - Create")
        print("[R] - Read")
        print("[U] - Update")
        print("[D] - Delete")
        print("[X] - Exit")
        choice = input("Enter choice: ").strip().upper()

        if choice == 'C':
            m.create()
        elif choice == 'R':
            m.read()
        elif choice == 'U':
            m.update()
        elif choice == 'D':
            m.delete()
        elif choice == 'X':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    menu()