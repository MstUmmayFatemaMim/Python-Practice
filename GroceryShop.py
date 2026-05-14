# Model: দোকানের স্টক এবং হিসাব
class ShopModel:
    def __init__(self):
        self.items = {"চাল": 50, "ডাল": 120, "তেল": 200}  # জিনিসের দাম
        self.orders = []  # গ্রাহকের অর্ডার

    def add_order(self, item, quantity):
        if item in self.items:
            self.orders.append({"item": item, "quantity": quantity})
            return True
        return False

    def calculate_bill(self):
        total = 0
        for order in self.orders:
            total += self.items[order["item"]] * order["quantity"]
        return total

# View: মেনু এবং বিল দেখানো
class ShopView:
    def show_menu(self, items):
        print("\nদোকানের মেনু:")
        for item, price in items.items():
            print(f"{item}: {price} টাকা/কেজি")

    def show_order(self, item, quantity):
        print(f"অর্ডার যোগ হয়েছে: {item} - {quantity} কেজি")

    def show_bill(self, total):
        print(f"মোট বিল: {total} টাকা")

# Controller: Model এবং View-এর মধ্যে সমন্বয়
class ShopController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def display_menu(self):
        self.view.show_menu(self.model.items)

    def place_order(self, item, quantity):
        if self.model.add_order(item, quantity):
            self.view.show_order(item, quantity)
        else:
            print(f"দুঃখিত, {item} আমাদের দোকানে নেই।")

    def show_bill(self):
        total = self.model.calculate_bill()
        self.view.show_bill(total)

# প্রোগ্রাম চালানো
def main():
    model = ShopModel()
    view = ShopView()
    controller = ShopController(model, view)

    # মেনু দেখানো
    controller.display_menu()

    # গ্রাহকের অর্ডার
    controller.place_order("চাল", 2)
    controller.place_order("ডাল", 1)

    # মোট বিল দেখানো
    controller.show_bill()

if __name__ == "__main__":
    main()