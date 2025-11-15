## This program is a rock paper scissor game
import random
def get_choice():
    player_choice=input('Enter your choice from these 3 options (rock,paper,scissors)? ')
    options=['rock','paper','scissors']
    computer_choice=random.choice(options)
    pass_choices={'player_choice':player_choice,'computer_choice':computer_choice}
    return pass_choices

def check_result(player_choice,computer_choice):
    if player_choice==computer_choice:
        return('Game is tie')
    elif player_choice=='rock':
        if computer_choice=='scissors':
            return('Rock smashes scissors! You win')
        else:
            return('Paper covers rocks You lose')
    elif player_choice=='scissors':
        if computer_choice=='paper':
            return('Scissors cuts paper! You win')
        else:
            return('Rock smashes scissors You lose')
    elif player_choice=='paper':
        if computer_choice=='rock':
            return('Rock covers paper! You win')
        else:
            return('Scissors cuts paper, You lose')
    else:
        return('Wrong User input')

result1=get_choice()
result2=check_result(result1['player_choice'],result1['computer_choice'])
print(result2)
