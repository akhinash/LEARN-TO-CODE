print("hello from greeting module")

def welcome(name):
    print(f"Welcome, {name}!")


if __name__ == "__main__":
    print("This runs only if greeting.py is executed.")
    welcome("Don")