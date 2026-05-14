#####   Show is vs == behavior with strings.
## Same value retuen true different value return false
name="mim"
nick="mim"
print(name == nick)
print(id(name),id(nick))
print(name is nick)
print(id(name),id(nick))
