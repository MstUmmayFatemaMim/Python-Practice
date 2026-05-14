fruits = ["apple", "banana", "mango","orange"]
print(fruits[0])  # Output: apple (first item)
print(fruits[1])  # Output: banana
print(fruits[-1])
print(fruits[0:2])  # Output: ['apple', 'banana'] (items at index 0 and 1)
print(fruits[1:])   # Output: ['banana', 'mango', 'orange'] (from index 1 to end)
print(fruits[:4])   # Print all index
print(fruits[:2])   #(items at index 0 and 1)
fruits[1] = "kiwi"  # Replace banana with kiwi
print(fruits)  # Output: ['apple', 'kiwi', 'mango']
fruits.append("lichi")  # Add lichi to the end
print(fruits)  # Output: ['apple', 'banana', 'mango']
fruits.insert(1, "guava")  # Add guava at index 1
print(fruits)
fruits.remove("guava")  # Remove guava
print(fruits)  # Output: ['apple', 'kiwi', 'mango', 'orange', 'lichi']
fruits.pop(0)  # Remove item at index 0 (apple)
print(fruits)  # Output: ['kiwi', 'mango', 'orange', 'lichi']
# fruits.clear()  # Empty the list
# print(fruits)  # Output: []
print(len(fruits))  # Output: 4 (number of items)
fruits.sort()    # Sort alphabetically
print(fruits)    # Output: ['kiwi', 'lichi', 'mango', 'orange']
fruits.reverse()    # Reverse the list
print(fruits)       # Output: ['orange', 'mango', 'lichi', 'kiwi']
print("Another reverse way fruits list:")
print(sorted(fruits, reverse=True))  # New list, sorted in reverse
# Output: ['mango', 'banana', 'apple', 'apple']
print(fruits.count("apple"))  # Output: 0(apple not appears)
print(fruits.count("lichi"))  # Output: 1(lichi appears one times)
print(fruits.index("orange"))  # Output: 1 (orange's index 0)
print("Without indexing all fruits : ")
for fruit in fruits:
    print(f"Selling {fruit}") #f-string (short for “formatted string literal”)
print("With indexing all fruits : ")
for i in range(len(fruits)):
    print(f"Item {i}: {fruits[i]}")