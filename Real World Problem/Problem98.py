# ############    Track expenses using dictionary and calculate total.
# expenses = {
#     "rent":      5000,
#     "food":      2000,
#     "transport": 1000,
#     "internet":   500,
#     "entertain": 2000,
#     "savings for car":5000,
#     "savings for our future":5000
# }
#
# # Add new expense
# expenses["gym"] = 800       ####O(1)
# print("After add:", expenses)
#
# # Update expense
# expenses["food"] = 2500         ######### O(1)
# print("After update:", expenses)
#
# # Remove expense
# del expenses["gym"]         #########       O(1)
# print("After delete:", expenses)
#
# # Calculate total
# total = 0
# for amount in expenses.values():    # O(n)
#     total += amount
# print("Total:", total)

# ##########  Way 2 — Using sum() + function (cleaner)
# expenses = {
#     "rent":      5000,
#     "food":      2000,
#     "transport": 1000,
#     "internet":   500
# }
#
# def add_expense(category, amount):
#     if category in expenses:                    # O(1)
#         print(f"'{category}' exists. Use update instead.")
#     else:
#         expenses[category] = amount             # O(1)
#         print(f"'{category}' : {amount} added.")
#
# def update_expense(category, amount):
#     if category in expenses:                    # O(1)
#         expenses[category] = amount             # O(1)
#         print(f"'{category}' updated to {amount}.")
#     else:
#         print(f"'{category}' not found!")
#
# def remove_expense(category):
#     if category in expenses:                    # O(1)
#         del expenses[category]                  # O(1)
#         print(f"'{category}' removed.")
#     else:
#         print(f"'{category}' not found!")
#
# def calculate_total():
#     return sum(expenses.values())               # O(n)
#
# def show_expenses():
#     print("\n------- Expenses -------")
#     for category, amount in expenses.items():   # O(n)
#         print(f"{category:15} → {amount:>8}")
#     print(f"{'TOTAL':15} → {calculate_total():>8}")
#
# # ---- Test ----
# add_expense("gym", 800)
# update_expense("food", 2500)
# remove_expense("internet")
# show_expenses()

##############  Way 3 — Category wise grouping (nested dictionary)
expenses = {
    "Housing":   {"rent": 5000, "electricity": 800, "water": 300},
    "Food":      {"groceries": 2000, "dining": 1000},
    "Entertain": {"tour": 5000, "movie": 500},
    "Savings":{"hajj":2000,"umrah":2000,"buy a car":2000,}
}

def category_total(category):                   # O(m) m=items in category
    return sum(expenses[category].values())

def grand_total():
    total = 0
    for category in expenses:                   # O(n*m)
        total += category_total(category)
    return total

def show_expenses():
    print("\n======= Expense Report =======")
    for category, items in expenses.items():    # O(n*m)
        print(f"\n📁 {category}")
        for item, amount in items.items():
            print(f"   {item:15} → {amount:>8}")
        print(f"   {'Subtotal':15} → {category_total(category):>8}")
    print(f"\n{'GRAND TOTAL':>24} → {grand_total():>8}")

# Add expense to a category
expenses["Food"]["snacks"] = 500               # O(1)

# Add new category
expenses["Transport"] = {"Rent": 1000}   # O(1)

# Add new category
expenses["Health Issue"] = {"gym": 800}   # O(1)
show_expenses()

# ##########  Way 4 — Using defaultdict (no KeyError ever)
# from collections import defaultdict
#
# # defaultdict(int) → missing key auto starts at 0
# expenses = defaultdict(int)
#
# def add_expense(category, amount):
#     expenses[category] += amount    # O(1) — no need to check if key exists
#     print(f"Added {amount} to '{category}'. Total: {expenses[category]}")
#
# def remove_expense(category):
#     if category in expenses:        # O(1)
#         del expenses[category]      # O(1)
#         print(f"'{category}' removed.")
#     else:
#         print(f"'{category}' not found!")
#
# def calculate_total():
#     return sum(expenses.values())   # O(n)
#
# def show_expenses():
#     print("\n------- Expenses -------")
#     for category, amount in sorted(expenses.items(),
#                                    key=lambda x: x[1],
#                                    reverse=True):   # sorted by amount O(n log n)
#         print(f"{category:15} → {amount:>8}")
#     print(f"\n{'TOTAL':15} → {calculate_total():>8}")
#
# # ---- Test ----
# add_expense("rent",      5000)
# add_expense("food",      2000)
# add_expense("food",       500)   # adds to existing food → 2500
# add_expense("transport", 1000)
# remove_expense("transport")
# show_expenses()

# ##############  Way 5 — Full tracker with statistics (real project style)
# from collections import defaultdict
#
# expenses  = {}
# history   = []           # keeps log of every action
#
# def add_expense(category, amount):
#     if amount <= 0:
#         print("Amount must be positive!")
#         return
#     if category in expenses:            # O(1)
#         print(f"'{category}' exists. Use update.")
#         return
#     expenses[category] = amount         # O(1)
#     history.append(("ADD", category, amount))
#     print(f"✅ '{category}' : {amount} added.")
#
# def update_expense(category, amount):
#     if category not in expenses:        # O(1)
#         print(f"'{category}' not found!")
#         return
#     old = expenses[category]
#     expenses[category] = amount         # O(1)
#     history.append(("UPDATE", category, amount))
#     print(f"✅ '{category}' updated {old} → {amount}")
#
# def remove_expense(category):
#     if category not in expenses:        # O(1)
#         print(f"'{category}' not found!")
#         return
#     amount = expenses.pop(category)     # O(1)
#     history.append(("REMOVE", category, amount))
#     print(f"🗑️ '{category}' removed.")
#
# def statistics():
#     if not expenses:
#         print("No expenses yet!")
#         return
#
#     total   = sum(expenses.values())                        # O(n)
#     highest = max(expenses, key=lambda k: expenses[k])      # O(n)
#     lowest  = min(expenses, key=lambda k: expenses[k])      # O(n)
#     average = total / len(expenses)                         # O(1)
#
#     print("\n======= Expense Statistics =======")
#     print(f"{'Category':15} {'Amount':>8} {'% of Total':>12}")
#     print("-" * 38)
#
#     for cat, amt in sorted(expenses.items(),
#                            key=lambda x: x[1],
#                            reverse=True):                   # O(n log n)
#         bar     = "█" * (amt // 500)                        # visual bar
#         percent = amt / total * 100
#         print(f"{cat:15} {amt:>8}  {percent:>10.1f}%  {bar}")
#
#     print("-" * 38)
#     print(f"{'Total':15} {total:>8}")
#     print(f"{'Average':15} {average:>8.1f}")
#     print(f"{'Highest':15} {highest} ({expenses[highest]})")
#     print(f"{'Lowest':15} {lowest}  ({expenses[lowest]})")
#
# def show_history():
#     print("\n------- History -------")
#     for action, category, amount in history:    # O(h) h=history length
#         print(f"{action:8} | {category:15} | {amount}")
#
# # ---- Test ----
# add_expense("rent",      5000)
# add_expense("food",      2000)
# add_expense("transport", 1000)
# add_expense("internet",   500)
# add_expense("gym",        800)
# update_expense("food", 2500)
# remove_expense("gym")
#
# statistics()
# show_history()