import sys

position = 0
depth = 0
aim = 0

for line in sys.stdin.read().splitlines():
    command, number = line.split(" ")
    if command == "forward":
        position += int(number)
        depth += aim * int(number)
    elif command == "up":
        aim -= int(number)
    elif command == "down":
        aim += int(number)

print(position * depth)
