###########     Reverse words but keep their original order.

sen = "Hello World From Python"
words = sen.split()
print(words)
i = len(words) - 1

while i >= 0:
    while i < len(words):

        # reverse each word manually
        word = words[i]
        reversed_word = ""
        j = len(word) - 1
        while j >= 0:
            reversed_word += word[j]
            j -= 1

        print(reversed_word, end=" ")
        i += 1
        break
    i -= 2
print()