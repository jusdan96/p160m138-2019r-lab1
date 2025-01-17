import sys

def greet(new_greeted_name: str, shout_count: int = 1):
    return f"Hello, {new_greeted_name}{shout_count * '!'}"


if len(sys.argv) <= 2:
    print(greet(sys.argv[1]))
else:
    print(greet(sys.argv[1], int(sys.argv[2])))
