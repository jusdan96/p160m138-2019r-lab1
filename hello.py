import sys

def greet(greeted_name: str):
    return f"Hello, {greeted_name}!"

print(greet(sys.argv[1]))

