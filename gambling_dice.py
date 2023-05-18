

#generate dice
import random


user_dice_one = random.randrange(1,7)
user_dice_two = random.randrange(1,7)

print(user_dice_one)
print(user_dice_two)



#ask user deposit amount

#ask user wager amount

#display wager amount and balance

#roll both dice until
    #if roll 7 or 11 on first roll automatic win for user
    #if roll 3 on first roll user automatically losses 
    #otherwise hold the total of the two dice as target total
    #if user rolls 7, 11 or 3 on user losses 
    #if user gets match then user wins + balance

def roll_dice(dice_one, dice_two):
    total = 0
    total = dice_one + dice_two
    return total

user_total = roll_dice(user_dice_one, user_dice_two)

while True:
    turns = 0
    first_roll = 0
    first_roll = user_total
    if first_roll == 7 or first_roll == 11:
        print(f"You win! First Roll Total: {first_roll}")
        break
    elif first_roll == 3:
        print(f"Craps, you loose! Roll Total: {first_roll}")
        break
    else:
        second_roll = roll_dice()
        

    
    
        



