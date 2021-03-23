import random

num = random.randint(0, 100)
count = 0
num_users = 0
while True:
    num_users = int(input('Enter number from 1 to 100. Guess the number: '))
    count += 1
    if num_users == num:
        print(f'You guessed the number for {count} attempts.')
        if input('Try to play the game again? "yes|no": ') == 'yes':
            num = random.randint(0, 100)
            count = 0
        else:
            print('Thanks for the game.')
            break
    elif num_users > num:
        print('Your number must be less')
    elif num_users < num:
        print('Your number must be greater')
    else:
        print('This number is incorrect')
