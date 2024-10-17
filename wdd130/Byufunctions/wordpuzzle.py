#Word puzzle

word =str('pera')
guess = str(input('What is your guess? '))

while word != guess:

    if word.lower() == guess.lower():
        print("congratulations you win!")
    elif word != guess:
        print('You lose')
        guess = str(input('What is your guess? '))
    else:
        print('sorry your guess must have the same number of letters as the secret word')

print('Congratulation you win')