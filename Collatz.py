number = 3
steps = 0

for i in range(200):
    if number == 1:
        break
    if number % 2 == 0:
        number = number / 2
    else:
        number = number * 3 + 1
    steps += 1  # On incrémente le nombre de pas

if number == 1:
    print("It took", steps, "steps")
else:
    print("The number didn't reach 1 yet")