#Hi professor, i add a limited number of errors can only be 3 in the sense of writing a word that is a different number of characters than the secret word
#Welcome to this byu WORLDLE Hope you Enjoy
#Variables set
secret_word = 'baptism'
secret_word_lent = "_ " * len(secret_word) 
hint = ''
play_again =''
game_count = 1
error_count = 1
game =""
#Welcome Message
print("Welcome to the word guessing game!")
print("Welcome player to this wonderful word game, to have fun you must try a word that has the same number of characters as the secret word, you will only have three tries or the game will end! Good luck!")
print(f"Your hint is: {secret_word_lent}")

user_guess = str(input('What is your guess? '))

while play_again != 'no':
    
    if len(user_guess) == len(secret_word):
        while user_guess != secret_word:  
            
            for i in range(0, len(secret_word)):
                if user_guess[i] == secret_word[i]:
                    hint += user_guess[i].capitalize()
                elif user_guess[i] in secret_word:
                    hint += user_guess[i].lower()
                else:
                    hint += ' _'
            
            print('Your guess was not correct')
            print(f"Your hint is: {hint}" )
            hint = ''
            game_count += 1
            
            user_guess = str(input('What is your guess? '))
            
            if user_guess == secret_word:
                print('Congratulation you win')
                print(f'It took you {game_count} times')
    else:
           #Creativity if the user limitation to the numbers of errors
           while error_count <= 2 :
            if user_guess != secret_word:
                    print('Sorry, the guess must have the same number of letters as the secret word.')
                    error_count += 1
                    print(f"Your hint is: {secret_word_lent}")
                    user_guess = str(input('What is your guess? '))
            if user_guess == secret_word:
                print('Congratulation you win')
                game_count += 1
                print(f'It took you {game_count} times')
                
                error_count = 10
                
                    
            if error_count == 3:
                        print("I'm sorry ! Unfortunately you have exceeded the maximum number of attempts, try again later.")

    
   


    play_again = str(input('Do you wanna play again? yes/no '))
    if play_again == 'yes':
            print(f"Your hint is: {secret_word_lent}")
            user_guess = str(input('What is your guess? '))
            error_count = 0
    else:
            print('Thanks for playing')
    

        


