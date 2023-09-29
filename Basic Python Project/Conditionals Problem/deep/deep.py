answer = input(
    "What is the Answer to the Great Question of Life, the Universe, and Everything?"
)
answer = answer.lower().strip()
a = ["forty-two", "forty two", "42", 42]
print("Yes") if answer in a else print("No")
