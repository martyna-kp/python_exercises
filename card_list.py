# Define a function that checks if the average of the first and last card values or the middle card value is equal to the calculated average of the hand.

def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Does one of the approximate averages equal the `true average`?
    """

    return card_average(hand) == ((hand[0]+hand[-1])/2) or card_average(hand) == hand[len(hand)//2]


# Define a function that checks if the average of the even indexed card values is equal to the average of the odd indexed card values.

def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        bool: Are the even and odd averages equal?
    """

    even_cards = hand[::2]
    odd_cards = hand[1::2]

    even_average = sum(even_cards) / len(even_cards)
    odd_average = sum(odd_cards) / len(odd_cards)

    return even_average == odd_average


# Define a function that doubles the value of a Jack card in the last index position of the hand.

def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    Parameters:
        hand (list): The cards in the hand.

    Returns:
        list: The hand with Jacks (if present) value doubled.
    """
    if hand[-1] == 11:
        hand[-1] *= 2
    return hand
