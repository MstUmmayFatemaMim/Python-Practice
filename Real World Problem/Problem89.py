##########      Find duplicate numbers in a list.

nums = [1, 2, 3, 2, 4, 5, 1, 6,5]
seen = set()
duplicates = set()

for x in nums:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(list(duplicates)) # Output: [1, 2]
