words = ("A", "B", "C", "D", "E")
# or
words = "A", "B", "C", "D", "E"

try:
    words[0] = "a"
except TypeError:
    print("Immutable")

print(words[0])
