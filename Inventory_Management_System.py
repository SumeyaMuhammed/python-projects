class Inventory:
    def __init__(self):
        self.stock = {}

    def  add_item(self, item, quantity):
        self.stock[item] = quantity
        print("Item added.")

    def remove_item(self, item, quantity):
        previous_quantity = self.stock[item]   
        remove_quantity = quantity
        updated_quantity = int(previous_quantity) - int(remove_quantity)
        if updated_quantity != 0:
            self.stock[item] = updated_quantity
        else:
            del self.stock[item]
        print("removed! ")

    def check_stock(self):
        print(self.stock)
        
    def run(self):
            while True:
                print("1. view stock")
                print("2. add item")
                print("3. remove item")
                print("4. Exit.")
                choice = input("Please enter your choice: ")

                if choice == '1':
                    self.check_stock()
                elif choice == '2':
                    item = input("Enter item name: ")
                    item_key = f'{item}'
                    quantity = input("Enter the amount: ")
                    quantity_value = f'{quantity}'
                    self.add_item(item_key, quantity_value)
                elif choice == '3':
                    remove_item = input("Choose the item to remove? ")
                    remove_item_key = f'{remove_item}'
                    remove_quantity = f"{input('how much to remove? ')}"
                    self.remove_item(remove_item_key, remove_quantity)
if (__name__) == "__main__":
    inventory = Inventory()
    inventory.run()