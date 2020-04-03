import random  # for shuffling cards
families = ['Spade', 'Club', 'Heart', 'Diamond']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = {'Ace': 1, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10}


class Card:
    def __init__(self, suit, rank, value):
        self.suit = suit
        self.rank = rank
        self.value = value

    def print_card(self):
        """
        Prints a given card with its attributes.
        :return: nothing
        """
        line = '---------------'
        space_family = len(line)-5 - len(self.suit)
        blank_family = ' '*space_family
        space_rank = len(line)-5-len(self.rank)
        blank_rank = ' '*space_rank
        space_value = len(line)-7-len(str(self.value))
        blank_value = ' '*space_value
        print('---------------')
        print('|   ' + self.suit + blank_family + '|')
        print('|             |')
        print('|   ' + self.rank + blank_rank + '|')
        print('|             |')
        print('|     ' + str(self.value) + blank_value + '|')
        print('|             |')
        print('---------------')


class Deck:
    def __init__(self):
        self.deck = []
        for suit in families:  # Family of card taken.
            for rank in ranks:  # Rank assigned.
                value = values[rank]  # Rank mapped with is corresponding value.
                new_card = Card(suit, rank, value)  # New card object created.
                self.deck.append(new_card)  # Card object appended to the deck.
        print("Deck Ready")

    def shuffle(self):
        """
        Shuffles a newly created deck of card.
        :return: nothing
        """
        random.shuffle(self.deck)
        print("Deck Shuffled!")

    def print_deck(self):
        """
        Prints a deck of card
        :return: nothing
        """
        for card in self.deck:
            card.print_card()

    def deal(self):
        """
        Distributes two cards to each player.
        :return: A list, top two cards from the deck.
        """
        return [self.deck.pop(0), self.deck.pop(0)]

    def return_top_two(self):
        top_two_cards = [self.deck[0], self.deck[1]]
        return top_two_cards


class Hand:
    def __int__(self):
        self.hold_cards = []  # This list holds cards on the hand of a player.
        self.sum_of_cards = 0   # To keep track of the sum of all cards.
        self.aces = 0    # To keep track of aces so that its value can adjusted whenever necessary.

    def add_card(self, new_card_to_add):
        """
        Adds new card to the hand of a player.
        :param new_card_to_add: list that holds a deck of cards
        :return:
        """
        new_card_from_deck = new_card_to_add.pop(0)
        self.hold_cards.append(new_card_from_deck)

    def adjust_for_ace(self):
        pass

    # This is a temporary function only for testing purpose.
    def show_cards_on_hand(self):
        for hand_cards in self.cards:
            hand_cards.print_card()

class Chips:
    def __int__(self):
        self.total = 100  # you get 100 coins at the start
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


# Game play begins here.....
while True:
    # Game Opening
    print("========================")
    print("| Welcome To BlackJack |")
    print("========================")
    new_deck = Deck()  # Creating a new deck of cards.
    new_deck.shuffle()  # Deck shuffled.
    human_player = Hand()  # Human player created; Hand object.
    print("Before Dealing")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()
    card_dealt_to_human_player = new_deck.deal()
    print("Dealt to human player.")
    for cards in card_dealt_to_human_player:
        cards.print_card()
    print("After dealing.")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()
    human_player.add_card(card_dealt_to_human_player)
    human_player.add_card(card_dealt_to_human_player)

    '''
    computer_player = Hand()  # Computer player created; Hand object.
    print("Before Dealing")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()
    card_dealt_to_computer = new_deck.deal()
    print("Dealt to computer.")
    print("After dealing.")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()
    '''
    break
