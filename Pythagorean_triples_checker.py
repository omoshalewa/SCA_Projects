''' Allows the user to input the sides of any triangle in any order.
Return whether the triangle is a Pythagorean Triple or not.
Loop the program so the user can use it more than once without having to restart the program
    #a**2 + b**2 = c**2
'''


def pythagorean_checker():
    triple_checker = True
    while triple_checker:

        print("Do you want to know if a triangle is Pythagorean Triple?"
              "\nEnter the length of the sides of the triangle")

        input_check = True
        while input_check:
            triangle_sides = []

            try:
                a = int(input("Side 1: "))
                b = int(input("Side 2: "))
                c = int(input("Side 3: "))
            except ValueError:
                print("You have to enter a numerical value")
            else:
                triangle_sides.append(a)
                triangle_sides.append(b)
                triangle_sides.append(c)

                sorted_sides = sorted(triangle_sides)
                print(sorted_sides)

                if sorted_sides[0]**2 + sorted_sides[1]**2 == sorted_sides[2]**2:
                    print("Oh yeah, it's a pythagorean triple!")
                    input_check = False
                else:
                    print("Nope, it's not a pythagorean triple :(")
                    input_check = False

        check_again = input("\nDo you want to check again?\n"
                            "Type 'y' for yes or 'n' for no: ").lower()
        if check_again == 'n':
            print("I hope you got your answer")
            triple_checker = False


pythagorean_checker()