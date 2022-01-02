import sys


stdinput = sys.stdin.read().splitlines()

last_measurement = 0
num_higher_measurement = 0

for index in range(len(stdinput)):
    if len(stdinput) - index < 3:
        break

    measure = sum(map(int, stdinput[index : index + 3]))

    if index == 0:
        last_measurement = measure

    if measure > last_measurement:
        num_higher_measurement += 1

    last_measurement = measure

print(num_higher_measurement)
