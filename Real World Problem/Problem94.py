# ###########     Track inventory using dictionary.
inventory = {
    "apple":  50,
    "banana": 30,
    "mango":  20
}

# Add new item
inventory["grape"] = 15
print("After add:", inventory)

# Update quantity
inventory["apple"] += 10
print("After update:", inventory)

# Remove item
del inventory["banana"]
print("After delete:", inventory)

# Check if item exists
if "mango" in inventory:
    print("Mango is in stock:", inventory["mango"])


# ###########Way 2 — Nested dictionary (store price + quantity together)
#
# inventory = {
#     "apple":  {"price": 20, "quantity": 50},
#     "banana": {"price": 10, "quantity": 30},
#     "mango":  {"price": 50, "quantity": 20},
# }
#
# # Add new item
# inventory["grape"] = {"price": 30, "quantity": 15}
#
# # Update quantity
# inventory["apple"]["quantity"] += 10
#
# # Remove item
# del inventory["banana"]
#
# # Show all items
# print("\n------- Inventory -------")
# for item, info in inventory.items():
#     print(f"{item:10} | Price: {info['price']:>5} | Quantity: {info['quantity']:>5}")

# ###############Way 3 — Function based (most practical, real project style)
# inventory = {
#     "apple":  {"price": 20, "quantity": 50},
#     "banana": {"price": 10, "quantity": 30},
#     "mango":  {"price": 50, "quantity": 20},
# }
#
# def add_item(name, price, quantity):
#     if name in inventory:
#         print(f"'{name}' already exists. Use update instead.")
#     else:
#         inventory[name] = {"price": price, "quantity": quantity}
#         print(f"'{name}' added successfully.")
#
# def remove_item(name):
#     if name in inventory:
#         del inventory[name]
#         print(f"'{name}' removed successfully.")
#     else:
#         print(f"'{name}' not found!")
#
# def update_quantity(name, amount):
#     if name in inventory:
#         inventory[name]["quantity"] += amount
#         print(f"'{name}' quantity updated to {inventory[name]['quantity']}")
#     else:
#         print(f"'{name}' not found!")
#
# def show_inventory():
#     print("\n------- Inventory -------")
#     for item, info in inventory.items():
#         print(f"{item:10} | Price: {info['price']:>5} | Qty: {info['quantity']:>5}")
#     print("-------------------------")
#
# def low_stock(limit=15):
#     print(f"\n--- Items with quantity below {limit} ---")
#     for item, info in inventory.items():
#         if info["quantity"] < limit:
#             print(f"{item:10} | Quantity: {info['quantity']}")
#
# # ---- Test it ----
# add_item("grape", 30, 10)
# update_quantity("apple", -5)      # sold 5 apples
# remove_item("banana")
# show_inventory()
# low_stock(limit=15)

# ###########     Way 4 — Using get() + setdefault() (safe access)
# inventory = {
#     "apple":  {"price": 20, "quantity": 50},
#     "banana": {"price": 10, "quantity": 30},
# }
#
# # get() — safe access, no crash if key missing
# item = inventory.get("grape", "Not found")
# print(item)                         # → Not found  (no KeyError)
#
# # setdefault() — add only if not already present
# inventory.setdefault("mango", {"price": 50, "quantity": 20})
# inventory.setdefault("apple", {"price": 99, "quantity": 999})  # won't overwrite
#
# print("\n------- Inventory -------")
# for item, info in inventory.items():
#     print(f"{item:10} | Price: {info['price']:>5} | Qty: {info['quantity']:>5}")

# #############       Way 5 — Using Counter (quick quantity tracking)
# from collections import Counter
#
# # Imagine these are scanned items at a shop
# sold_items = ["apple", "banana", "apple", "mango", "apple", "banana"]
#
# sold_count = Counter(sold_items)
# print("Sold:", dict(sold_count))
#
# # Deduct from inventory
# inventory = {"apple": 50, "banana": 30, "mango": 20}
#
# for item, qty in sold_count.items():
#     if item in inventory:
#         inventory[item] -= qty
#
# print("After sales:", inventory)