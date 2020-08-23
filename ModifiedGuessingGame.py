def level(num_range, guess_limit, secret_number):
    print(f'Enter a number between 1 and {num_range}')
    guess_count = 0
    while guess_count < guess_limit:
        try:
            guess_count += 1
            guess = int(input('Guess a number: '))
            if guess in range(num_range + 1):
                if guess == secret_number:
                    print('You got it right!')
                    break
                elif guess != secret_number:
                    print('That was wrong')
                    print(f'You have {guess_limit - guess_count} guess left')
            else:
                print(f"Oops the number you entered isn't within the range of 1 and {num_range} ")
                print(f'You have {guess_limit - guess_count} guess left')
        except ValueError:
            print(f'''
Oops invalid value
Only numbers are allowed
Enter a number between 1 and {num_range}''')
            print(f'You have {guess_limit - guess_count} guess left')
    else:
        print('Game over!')
    return


play_game = True
print("""
Welcome to Guessing game!
How good are you at guessing?
Let's find out.
There are three levels: Easy, Medium and Hard.
All you have to do is type in the level you wanna play.
Here goes...""")

while play_game:
    game_level = input("What level do you want to play: ").lower()
    if game_level == 'easy':
        level(10, 6, 4)
        break

    elif game_level == 'hard':
        level(50, 3, 36)
        break

    elif game_level == 'medium':
        level(20, 4, 15)
        break

    else:
        print('''
You must choose a level
Enter either easy, medium or hard''')

