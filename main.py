import random

c = ['Rock', 'Paper', 'Scissors']

while True:
    user = input('Enter your choice (rock, paper, scissors): ').lower()

    if user not in ['rock', 'paper', 'scissors']:
        print('Invalid choice. Try again.\n')
        continue

    comp = random.choice(c).lower()

    print(f'You chose {user} and computer chose {comp}.')

    if (user == 'rock' and comp == 'paper') or \
       (user == 'paper' and comp == 'scissors') or \
       (user == 'scissors' and comp == 'rock'):
        print('You lose!\n')

    elif user == comp:
        print('It\'s a draw!\n')

    else:
        print('You win!\n')

    con = input('Do you want to continue? (y/n): ').lower()
    if con == 'n':
        print('Thanks for playing!')
        break
