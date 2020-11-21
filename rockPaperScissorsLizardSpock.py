import random

#the move with it's numerical value
move_with_val_dict = {'r':0, 'sp':1, 'p':2, 'l':3, 's':4}
#shortnames with their full, when user uses r
#it translates to 'rock'
short_name_with_full_dict = {'r':'rock','sp':'spock','l':'lizard','p':'paper','s':'scissors'}

#convert move's numeric value to it's name
def moveVal_to_move(number):
  if (number in move_with_val_dict.values()):
    return short_name_with_full_dict[list(move_with_val_dict.keys())[number]]

#convert move's name value to it's numeric value
def move_to_moveVal(name):
  if (name in list(move_with_val_dict.keys())):
    return move_with_val_dict[name]

dictionary = move_with_val_dict.keys()
        
def main():

    code = 1
    while code == 1:
        print("\n")
        u = input("Type in the character you want! r for 'rock', s for 'scissors' , l for 'lizard' , p for 'paper' ,sp for 'spock'  \n")
        user_input = str(u)

        player_number = move_to_moveVal(user_input)

        if user_input not in dictionary:
            print("That is an invalid choice! Please try again.")
        
        else:
            computer_choiceNUM = random.randrange(0, 4)
            computer_choice = moveVal_to_move(computer_choiceNUM)
            result = ((player_number) - (computer_choiceNUM)) % 5
            if result == 1 or result == 2:
                winner = 'You Won !!!'
            elif result == 3 or result == 4:
                winner = 'Computer Wins!'
            else:
                winner = 'It\'s a Tie!'

            print("You chose", moveVal_to_move(move_to_moveVal(user_input)))
            print("Computer chooses", computer_choice)
            print(winner)



print("Rock, Paper, Lizard, Scissors, Spock!")
print("Let's play!")

while True:
    main()
    
