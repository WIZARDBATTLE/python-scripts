import random

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
house = [deck[(random.randint(0,13))], deck[(random.randint(0,13))]]
hand = [deck[(random.randint(0,13))], deck[(random.randint(0,13))]]

if input("Start Blackjack? Y/N") == "Y" or "y":
    print(f"Your Hand: {hand}")
    print(f"House's Hand: {house[0]}")
    while sum(hand) < 21:
        if input("Hit or Stay?") == "Hit" or "hit":
            hand.append(deck[(random.randint(0,13))])
            print(f"Your Hand: {hand}")
            if sum(hand) > 21 and (11 in hand):
                for each in hand:
                    if each == 11:
                        hand[each] = 1
        else:
            break
    house.append(deck[(random.randint(0,13))])
    print(f"House's Hand: {house}")
    if sum(hand) == 21 or (sum(hand) < 21 and sum(house) < sum(hand)) or sum(house) > 21:
        print("You Win!")
    elif sum(hand) > 21 or (sum(hand) < 21 and sum(house) > sum(hand)):
        print("You Lose! Sorry bub")