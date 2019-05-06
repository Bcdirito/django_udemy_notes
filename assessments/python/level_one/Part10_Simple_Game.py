###########################
## PART 10: Simple Game ###
### --- CODEBREAKER --- ###
## --Nope--Close--Match--  ##
###########################

# It's time to actually make a simple command line game so put together everything
# you've learned so far about Python. The game goes like this:

# 1. The computer will think of 3 digit number that has no repeating digits.
# 2. You will then guess a 3 digit number
# 3. The computer will then give back clues, the possible clues are:
#
#     Close: You've guessed a correct number but in the wrong position
#     Match: You've guessed a correct number in the correct position
#     Nope: You haven't guess any of the numbers correctly
#
# 4. Based on these clues you will guess again until you break the code with a
#    perfect match!

# There are a few things you will have to discover for yourself for this game!
# Here are some useful hints:

# Try to figure out what this code is doing and how it might be useful to you
import random
digits = list(range(10))
random.shuffle(digits)
winning_num = digits[:3]
# print(winning_num)

def num_checker(comp_num):
    matches = 0
    
    while matches < 3:
        user_guess = input("What is your guess? ")
        user_num = list(user_guess)
        matches = 0
        found = 0
        for i in range(len(comp_num)):
            if comp_num[i] == int(user_num[i]):
                matches += 1
            elif int(user_num[i]) in comp_num:
                found += 1
        
        if matches == 0 and found == 0:
            print("Nope: You haven't guess any of the numbers correctly")
        elif matches == 1 or matches == 2:
            print("Match: You've guessed a correct number in the correct position")
        elif found > 0:
            print("Close: You've guessed a correct number but in the wrong position")
    else:
        return "Match! You Win!"

    

print(num_checker(winning_num))
# Think about how you will compare the input to the random number, what format
# should they be in? Maybe some sort of sequence? Watch the Lecture video for more hints!
