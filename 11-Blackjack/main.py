import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card




def calculate_score(cards):

    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)




def compare(user_score , dealer_score):
    if user_score == dealer_score:
        return "draw"

    elif dealer_score == 0:
        return "lose"

    elif user_score == 0:
        return "win"

    elif user_score > 21:
        return "lose"

    elif dealer_score > 21:
        return "win"

    elif user_score > dealer_score:
        return "win"

    else:
        "lose"



def the_game():
    print(art.logo)

    user_cards = []
    dealer_cards = []
    dealer_score = -1
    user_score = -1
    gameOVER = False
    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not gameOVER:

        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            game0VER = True

        else:
            ans_of_user = input("Type 'y' to get another card, type 'n' to pass: ")
            if ans_of_user == "y":
                user_cards.append(deal_card())
            else:
                gameOVER = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {dealer_cards}, final score: {dealer_score}")
        print(compare(user_score, dealer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    the_game()