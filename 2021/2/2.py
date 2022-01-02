import sys

position = 0
depth = 0

for line in sys.stdin.read().splitlines():
    command, number = line.split(" ")
    if command == "forward":
        position += int(number)
    elif command == "up":
        depth -= int(number)
    elif command == "down":
        depth += int(number)

print(position * depth)
