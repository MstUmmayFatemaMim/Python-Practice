# রাহিমের সহজ বাজার হিসাব প্রোগ্রাম
for i in range(3):

    def calculate_bill():
        name = input("What is your name? ")
        # পণ্যের তথ্য নেওয়া
        item = input("Which item do you want to buy? ")
        quantity = int(input(f"How many {item} do you want to buy? "))
        price_per_item = int(input(f"Tell me per piece {item} per item? "))

        # মোট বিল হিসাব
        total_bill = quantity * price_per_item

        # ছাড় হিসাব (৫০০ টাকার বেশি হলে ১০% ছাড়)
        discount = 0
        if total_bill > 500:
            discount = total_bill * 0.1

        final_amount = total_bill - discount

        # ফলাফল দেখানো
        print("\n--- হিসাবের বিবরণ ---")
        print(f"ক্রেতার নাম: {name}")
        print(f"পণ্য: {quantity} টি {item} (প্রতি টি {price_per_item} টাকা)")
        print(f"মোট বিল: {total_bill} টাকা")
        print(f"ছাড়: {discount} টাকা")
        print(f"পরিশোধ করতে হবে: {final_amount} টাকা")
        print("ধন্যবাদ, আবার আসবেন!")

        print(name, "এর কেনাকাটা রেকর্ড করা হলো!")

# প্রোগ্রাম চালানো
    calculate_bill()