bottle_number = 99
while bottle_number > 0:
    if bottle_number == 1:
        print(f"{bottle_number} bottle of beer on the wall."
              f"Take one down, pass in around. {bottle_number - 1} bottle of beer on the wall")
        break
    else:
        print(f"{bottle_number} bottles of beer on the wall."
              f"Take one down, pass in around. {bottle_number - 1} bottles of beer on the wall")
        bottle_number -= 1


