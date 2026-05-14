######      Count the number of words in a sentence.
text = "hello world from python"
text1=text.split()
print(text1)
count=0
for letter in text1:
    count+=1
print(count)