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

    # This a temporary function, removing it won't break your program.
    def return_card_rank(self):
        return self.rank


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

    # This function is only for testing purpose
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

    # You can remove this method
    def return_top_two(self):
        top_two_cards = [self.deck[0], self.deck[1]]
        return top_two_cards


class Hand:
    def __init__(self):
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
        """
        counts the number of aces held and finds sum of all cards except Ace
        """
        self.aces = 0
        self.sum_of_cards = 0
        for h_card in self.hold_cards:
            if h_card.rank == 'Ace':
                self.aces += 1
            else:
                self.sum_of_cards += h_card.value

    # This is a temporary function only for testing purpose.
    def show_cards_on_hand(self):
        for hand_cards in self.hold_cards:
            hand_cards.print_card()

    # This is a temporary function
    def return_no_of_aces(self):
        return self.aces


class Chips:
    def __init__(self):
        self.total = 0  # you get 100 coins at the start
        self.bet = 0

    def win_bet(self):
        pass

    def lose_bet(self):
        pass


def take_bet():
    # Player must buy chips before sitting for any game.
    while True:
        if new_chip.total == 0:
            try:
                player_total_chips = int(input("Enter total chips you have : "))
                if player_total_chips <= 0:
                    raise Exception
            except ValueError:
                print("Invalid! Enter a positive number.")
                continue
            except Exception:
                print("Invalid Amount Entered!")
                continue
            # else block runs only when try block doesn't throw an exception.
            else:
                new_chip.total += player_total_chips
                print("Thank you!")
                break
        # This is just to make sure that the program doesn't get stuck here due to some unexpected reason.
        else:
            break
    # Ask player to set bet for each round; bet is successful only if the amount is available in his bank
    while True:
        if new_chip.total > 0:
            try:
                player_bet = int(input("Enter your bet for this round : "))
                if player_bet > new_chip.total:
                    raise Exception
            except ValueError:
                print("Invalid! Enter a positive number")
            except Exception:
                print("Sorry! You don't have enough money.")
                print(f'You have {new_chip.total}')
            else:
                new_chip.bet += player_bet
                print("Thank you!")
                break
        # To avoid program from getting stuck here due to some unexpected reasons.
        else:
            break


def hit(card_deck, hand):
    """
    If player hits, topmost card of the deck goes to player's hand.
    """
    hand.hold_cards.append(card_deck.deck.pop(0))


def hit_or_stand(card_deck, hand):
    """
    deck : deck of playing cards; Class Deck()'s attribute 'deck'
    hand : hand of a player; Hand() object

    """
    ask = str(input("Would you like to hit? (Y/N)"))
    if ask.upper() == 'Y':
        hit(card_deck=card_deck, hand=hand)
    else:
        return False
    return True


def show_some(player, dealer):
    print("Dealer's Card")
    print("=============")
    dealer.hold_cards[0].print_card()
    print("__________________________")
    print("Player's Card")
    for all_cards in player.hold_cards:
        all_cards.print_card()


def show_all(player, dealer):
    print("Dealer's Card")
    print("=============")
    for all_cards in dealer.hold_cards:
        all_cards.print_card()
    print("____________________________________________________________")
    print("Player's Card")
    print("==============")
    for all_cards in player.hold_cards:
        all_cards.print_card()


def player_busts():
    human_player.adjust_for_ace()  # Adjusting the number of Aces and sum the cards except Aces.
    if (human_player.sum_of_cards + human_player.aces*11) > 21:
        if (human_player.sum_of_cards + human_player.aces*1) > 21:
            return True
        else:
            return False
    else:
        return False


def player_wins():
    pass


def dealer_busts():
    computer_player.adjust_for_ace()
    if (computer_player.sum_of_cards + computer_player.aces*11) > 21:
        if(computer_player.sum_of_cards + computer_player.aces*1) > 21:
            return True
        else:
            return False
    else:
        return False


def dealer_keeps_hitting():
    computer_player.adjust_for_ace()
    if (computer_player.sum_of_cards + computer_player.aces*11) > 17:
        if(computer_player.sum_of_cards + computer_player.aces*1) <= 17:
            return True
        else:
            return False
    else:
        return True


def dealer_wins():
    pass


def push():
    pass


# Game play begins here.....
while True:
    # Game Opening
    print("========================")
    print("| Welcome To BlackJack |")
    print("========================")
    new_deck = Deck()  # Creating a new deck of cards.
    # new_deck.shuffle()  # Deck shuffled.

    # Ask for bet
    new_chip = Chips()
    print(f'Total={new_chip.total}')
    take_bet()  # Take bet from player

    human_player = Hand()  # Human player created; Hand object.
    # This section is for dealing card to human player
    # You can remove this section
    print("Before Dealing")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()

    # Keep this line
    card_dealt_to_human_player = new_deck.deal()

    # remove this section
    print("Dealt to human player.")
    for cards in card_dealt_to_human_player:
        cards.print_card()
    print("After dealing.")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()

    # Keep these lines
    human_player.add_card(card_dealt_to_human_player)
    human_player.add_card(card_dealt_to_human_player)

    # Remove these lines
    print("Card Held by Human player")
    human_player.show_cards_on_hand()

    # This section is for dealing card to computer player
    computer_player = Hand()  # Computer player created; Hand object.

    # You can remove this part
    print("Before Dealing")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()

    # Keep this line
    card_dealt_to_computer = new_deck.deal()

    # You can remove this section
    print("Dealt to computer.")
    for cards in card_dealt_to_computer:
        cards.print_card()
    print("After dealing.")
    top_two = new_deck.return_top_two()
    for cd in top_two:
        cd.print_card()

    # You must keep these lines
    computer_player.add_card(card_dealt_to_computer)
    computer_player.add_card(card_dealt_to_computer)

    # You can remove this part
    print("Card Held by Computer")
    computer_player.show_cards_on_hand()
    # Show no. of Aces in Hand
    # This is for testing purpose
    print("Before Adjusting")
    # aces_held = human_player.return_no_of_aces()
    print(f"No of Aces= {human_player.aces}")
    print("After Adjusting")

    # You must keep these lines
    human_player.adjust_for_ace()
    computer_player.adjust_for_ace()

    # You can remove these lines
    aces_held = human_player.return_no_of_aces()
    print(f"No of Aces= {human_player.aces}")

    # Keep this line
    # To Show Dealer's one card and player's both cards.
    show_some(player=human_player, dealer=computer_player)

    # This for testing at the moment.
    # To show all cards
    show_all(player=human_player, dealer=computer_player)

    # Ask player if he wishes to hit or stand.
    # You must keep this section.
    human_playing = True
    while human_playing:
        human_playing = hit_or_stand(card_deck=new_deck, hand=human_player)
        if human_playing is True:
            # Before going for next hit let the player check his card once more.
            show_some(player=human_player, dealer=computer_player)
            if player_busts() is True:  # To check if player busted.
                human_playing = False
                # Might have to come back here...

    # To check if hit is working or not; you can remove it
    human_player.show_cards_on_hand()

    # To check if hitting works for dealer or not.
    print("Before Dealer's Turn")
    computer_player.show_cards_on_hand()

    # Once Human player stands; dealer's turn begins.
    computer_playing = True
    while computer_playing:
        if dealer_keeps_hitting() is True:
            hit(card_deck=new_deck, hand=computer_player)
        else:
            computer_playing = False

    # This is just for testing; you can remove this section.
    print("After Dealer is done hitting")
    computer_player.show_cards_on_hand()

    break
