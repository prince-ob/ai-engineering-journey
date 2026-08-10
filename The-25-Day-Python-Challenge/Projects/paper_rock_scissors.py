import random
print('Hello world!')

symbols: dict[str, str] = {'rock': '🪨',
                          'paper': '📄',
                          'scissors': '✂️'}

player_choice: str = input('Choose rock (🪨), paper (📄) or scissors (✂️ ): ').strip().lower()
computer_choice: str = random.choice(tuple(symbols))
# print(symbols[player_choice]) #if a player should type paper it will become print(symbols[paper] and the result is 📄 and this is a way of accessing value of a key in dict)

# print(tuple(symbols))
print('\nResults')
print('--------------------')
print(f"You:       {symbols[player_choice]}  {player_choice}")
print(f"Computer:  {symbols[computer_choice]}  {computer_choice}")
print('--------------------')

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == 'rock' and computer_choice == 'scissors':
    print("You won with rock! 🪨")
elif player_choice == 'paper' and computer_choice == 'rock':
    print("You won with paper! 📄")
elif player_choice == 'scissors' and computer_choice == 'paper':
    print('You won with scissors! ✂️')
else:
    print("Computer wins! ")