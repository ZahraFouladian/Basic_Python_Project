Greeting = input("Greeting:")
Greeting = Greeting.lower().lstrip()
if Greeting.startswith("hello"):
    print("$0")
elif Greeting.startswith("h"):
    print("$20")
else:
    print("$100")
