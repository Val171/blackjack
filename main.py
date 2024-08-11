card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
import random
from enum import Enum

class Result(Enum):
    WIN = 1
    DRAW = 2
    LOSS = 3
    IN_PROGRESS = 4

start = input("Letttsssssssss get ready to GAMBLE! y or n: ").lower()

player_card = list(random.choices(card, k = 2))      #sample instead of choices to choose without replacement. choices chooses with replacement
computer_hand = list(random.choices(card, k = 1))

def match_result(end = False):

    player_score = sum(player_card)
    comp_score = sum(computer_hand)

    # print(player_score)
    # print(comp_score)

    if player_score > 21:
        return Result.LOSS

    elif player_score == 21:
        return Result.WIN

    if comp_score > 21:
         return Result.WIN

    if end:

        if player_score > comp_score:
            return Result.WIN

        elif comp_score > player_score:
            return Result.LOSS

        else:
            return Result.DRAW

    else:
        return Result.IN_PROGRESS

def check_result(result):
     match result:
        case Result.WIN:
            print("You win!")
        case Result.DRAW:
            print("It's a draw!")
        case Result.LOSS:
            print("You lose.")


if start == "y":
    # print("hi") #filler
    print(f'Your cards: {player_card}')
    print(f"Computer's cards are {computer_hand}")

    while True:
        result = match_result(end = False)
        if result == Result.IN_PROGRESS:
            get_another = input("Do you wish to draw another card? y or n: ").lower()

            if get_another == "n":

                print(f"Your final hand is {player_card}")

                result = match_result(end = True)
                check_result(result)


            elif get_another == "y":

                player_card.append(random.choice(card))
                computer_hand.append(random.choice(card))

                print(f"Your updated hand is {player_card}")

                result = match_result()
                if result != Result.IN_PROGRESS:
                    check_result(result)
                    break


