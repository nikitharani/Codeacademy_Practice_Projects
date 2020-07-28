# The Code below code is a part of code academy project - game of chances
# There are 4 games in total: Coin_Flip, Cho-Han, High/Low card game and Roulette

import random

money = 100


# Coin flip game
def Coin_Flip(guess, bet_amount):
    global money

    if bet_amount >= money:
        print("Bet cannot exceed account balance!")
        print("Please lower your bet_amount.")
        print("Bet must be less than " + str(money) + " credits.")
        print("Thanks for playing!")
    else:
        print("Welcome to Coin Flip Game!...your account balance is : " + str(money))
        print("It's time to flip a coin!")
        print("You bet " + str(bet_amount) + " credits on " + str.lower(guess) + ".")

        # Random integer to represent heads/tails
        coin = random.randint(0, 1)

        # Assigning Heads/Tails to the number generated.
        if coin == 0:
            coin_face = "heads"
        else:
            coin_face = "tails"

        # Printing results of the "coin flip"
        print("Flipping the coin...")
        print("Coin lands on...... " + coin_face + "!")

        # Check if the bet is won/loss
        if str.lower(guess) == coin_face:
            print("You win! " + str(bet_amount) + " credits have been added to your account!")
            money += bet_amount
            print("Your new account balance is: " + str(money) + " credits.")
            print("Thanks for playing! See you Again!")
        else:
            print("You lose! " + str(bet_amount) + " credits have been subtracted from your account!")
            money -= bet_amount
            print("Your new account balance is: " + str(money) + " credits")
            print("Thanks for playing! Better luck next Time!")

    print("------------------------------")


# Cho-Han game
def Cho_Han(guess, bet_amount):
    global money
    if bet_amount >= money:
        print("Bet cannot exceed account balance!")
        print("Please lower your bet_amount.")
        print("Bet must be less than " + str(money) + " credits.")
        print("Thanks for playing!")
    else:
        print("Welcome to Cho-Han game!...your account balance is : " + str(money))
        print("In this game, you must guess the sum of two dice rolls is either even or odd.")
        print("You guessed: " + str(str.upper(guess)) + " and bet " + str(bet_amount) + " credits.")

        # Roll dice and find the total
        die_1 = random.randint(1, 6)
        die_2 = random.randint(1, 6)
        total = die_1 + die_2

        print("Rolling die......")
        print("Die 1: " + str(die_1))
        print("Die 2: " + str(die_2))
        print("Sum of roll: " + str(total))

        # Assign odd/even value to die roll (mod 2 being 0 means even number)
        if total % 2 > 0:
            result = "odd"
        else:
            result = "even"

        # Did the player win?
        if str.lower(guess) == result:
            print("You win! " + str(bet_amount) + " credits have been added to your account!")
            money += bet_amount
            print("Your new account balance is: " + str(money) + " credits.")
            print("Thanks for playing! See you Again!")
        else:
            print("You lose! " + str(bet_amount) + " credits have been subtracted from your account!")
            money -= bet_amount
            print("Your new account balance is: " + str(money) + " credits.")
            print("Thanks for playing! Better luck next Time!")
    print("------------------------------")


# Cards game
def Cards(bet_amount):
    global money
    if bet_amount >= money:
        print("Bet cannot exceed account balance!")
        print("Please lower your bet_amount.")
        print("Bet must be less than " + str(money) + " credits.")
        print("Thanks for playing!")
    else:
        payout = 0
        print("Welcome to the cards game!...your account balance is : " + str(money))
        print("Do you think you can get a higher card than me? Let's find out!")

        # 4 suits of cards, each with 13 cards in them
        spades = list(range(1, 14))
        hearts = list(range(1, 14))
        diamonds = list(range(1, 14))
        clubs = list(range(1, 14))

        # full deck of cards
        card_deck = spades + hearts + diamonds + clubs

        # player 1 draws a card
        player1_draw = random.randint(0, 51)
        player1_card = card_deck[player1_draw]

        # changing the display for the face cards
        if player1_card == 1:
            player1_card_disp = "A"
        elif player1_card == 11:
            player1_card_disp = "J"
        elif player1_card == 12:
            player1_card_disp = "Q"
        elif player1_card == 13:
            player1_card_disp = "K"
        else:
            player1_card_disp = player1_card
        print("You reach into the deck of cards and pull out a " + str(player1_card_disp) + ".")

        # remove the card player 1 drew from the deck:
        card_deck2 = card_deck[:player1_draw] + card_deck[player1_draw + 1:]
        player2_draw = random.randint(0, 50)
        player2_card = card_deck2[player2_draw]
        if player2_card == 1:
            player2_card_disp = "A"
        elif player2_card == 11:
            player2_card_disp = "J"
        elif player2_card == 12:
            player2_card_disp = "Q"
        elif player2_card == 13:
            player2_card_disp = "K"
        else:
            player2_card_disp = player2_card
        print("I reach into the deck of cards and pull out a " + str(player2_card_disp) + ".")

        # determine the winner:
        if player1_card > player2_card:
            print("You win!")
            print(str(bet_amount) + " credits have been added to your account.")
            money += bet_amount
            print("Your new account balance is: " + str(money) + " credits.")
            print("Thanks for playing! See you Again!")
        elif player1_card < player2_card:
            print("You lose!")
            print(str(bet_amount) + " credits have been subtracted from your account.")
            payout += -1 * bet_amount
            money += payout
            print("Your new account balance is: " + str(money) + " credits.")
            print("Thanks for playing! Better luck next Time!")
        else:
            print("It's a tie!")
            print("No money has been added or subtracted from your account.")
            print("Thanks for playing! Try Again!")

    print("------------------------------")


# Roulette
def Roulette(guess, bet_amount):
    global money
    if bet_amount >= money:
        print("Bet cannot exceed account balance!")
        print("Please lower your bet_amount.")
        print("Bet must be less than " + str(money) + " credits.")
        print("Thanks for playing!")
    else:
        print("Welcome to the Roulette game!...your account balance is : " + str(money))
        payout = 0

        # Create our roulette "wheel":
        roulette_numbers = list(range(0, 38))
        roulette_ball = random.randint(0, 37)

        # Convert guess to a string:
        guess = str(guess)

        # Create the display numbers:
        if roulette_ball == 0:
            roulette_display_num = "0"
        elif roulette_ball == 37:
            roulette_display_num = "00"
        else:
            roulette_display_num = str(roulette_ball)

        # Bet names
        Red_list = [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32, 34, 36]
        Black_list = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]
        first_column = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]
        second_column = [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]
        third_column = [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]

        # Single number -- win if ball lands on chosen number
        # 0 bet -- only win if lands on 0
        # 00 bet -- only win if lands on 00

        # Determine if the player wins:
        print("You guessed that the ball would land on: " + str.lower(guess))
        print("The ball is going around the wheel...")
        print("It lands on " + str(roulette_display_num) + ".")
        if (str.lower(guess) == "red" and roulette_ball in Red_list):  # if it's the colour guess
            print("It's red.")
            print("You win!")
            payout += bet_amount
        elif (str.lower(guess) == "black" and roulette_ball in Black_list):  # if it's the colour guess
            print("It's black.")
            print("You win!")
            payout += bet_amount
        elif (str.lower(guess) == "odd" and roulette_ball % 2 > 0):  # if it's the odd/even guess
            print("It's Odd")
            print("You win!")
            payout += bet_amount
        elif (str.lower(guess) == "even" and roulette_ball % 2 == 0):  # if it's the odd/even guess
            print("It's Even")
            print("You win!")
            payout += bet_amount
        elif ((str.lower(guess) == "first" or str.lower(guess) == "1st") and roulette_ball in first_column) or (
                (str.lower(guess) == "second" or str.lower(guess) == "2nd") and roulette_ball in second_column) or (
                (str.lower(guess) == "third" or str.lower(
                    guess) == "3rd") and roulette_ball in third_column):  # if it's the colum number guess
            print("You win!")
            payout += 2 * bet_amount
        elif str.lower(guess) == roulette_display_num:  # if it's the number guess
            print("You win!")
            payout += 35 * bet_amount
        else:
            print("You lose!")
            payout += -1 * bet_amount
        money += payout

        # Payout print:
        if payout < 0:
            print(str(abs(payout)) + " credits have been subtracted from your account!")
            print("Your new account balance is: " + str(money) + " credits")
            print("Thanks for playing! Better luck next Time!")
        else:
            print(str(payout) + " credits have been added to your account.")
            print("Your new account balance is: " + str(money) + " credits")
            print("Thanks for playing! See you Again!")

    print("------------------------------")


# You will have to manually call each of the functions currently
# Each function requires two arguments: a guess and a bet_amount
# Except for the cards function, which only requires a bet_amount

# Call your game of chance functions here
if __name__ == "__main__":
    # Coin_game demo
    Coin_Flip("HEads", 5)

    # Ch0_haum game demo
    Cho_Han("eVen", 2)

    # Cards game demo
    Cards(10)

    # Roulette game demo
    Roulette("red", 50)

