import sys

def greet(new_greeted_name: str):
    return f"Hello, {new_greeted_name}!"

print(greet(sys.argv[1]))

