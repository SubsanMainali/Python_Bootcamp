from IPython.display import clear_output
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

    def __del__(self):
        pass


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

    def deal(self):
        """
        Distributes two cards to each player.
        :return: A list, top two cards from the deck.
        """
        return [self.deck.pop(0), self.deck.pop(0)]


class Hand:
    def __init__(self):
        self.hold_cards = []  # This list holds cards on the hand of a player.
        self.sum_of_cards = 0   # To keep track of the sum of all cards.
        self.aces = 0    # To keep track of aces so that its value can adjusted whenever necessary.
        self.sum = 0  # Sum including Ace

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


class Chips:
    def __init__(self):
        self.total = 0  # you get 100 coins at the start
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total = self.total - self.bet


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
                new_chip.total = player_total_chips
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
                new_chip.bet = player_bet
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
    deck : deck of playing cards; Class Deck() type object.
    hand : hand of a player; Hand() object

    """
    ask = str(input("Would you like to hit? (Y/N)"))
    if ask.upper() == 'Y':
        hit(card_deck=card_deck, hand=hand)
    else:
        return False
    return True


def show_some(player, dealer):
    """
    Shows all the cards of a player but only one card of the dealer.
    """
    print("Dealer's Card")
    print("=============")
    dealer.hold_cards[0].print_card()
    print("__________________________")
    print("Player's Card")
    for all_cards in player.hold_cards:
        all_cards.print_card()


def show_all(player, dealer):
    """
    Shows all the cards in both player's hand.
    """
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
    """
    True if player busts, otherwise False.
    """
    human_player.adjust_for_ace()  # Adjusting the number of Aces and sum the cards except Aces.
    if (human_player.sum_of_cards + human_player.aces*11) > 21:
        if (human_player.sum_of_cards + human_player.aces*1) > 21:
            return True
        else:
            human_player.sum = human_player.sum_of_cards + human_player.aces*1
            return False
    else:
        human_player.sum = human_player.sum_of_cards + human_player.aces*11
        return False


def player_wins():
    """
    Takes necessary actions if player wins.
    """
    print("+++++++++++++++++++++++++++++")
    print("| Congratulations! You won. |")
    print("+++++++++++++++++++++++++++++")
    new_chip.win_bet()  # Won amount added to player's total amount.
    print(f'Your total sum = {new_chip.total}$')


def dealer_busts():
    """
    True if computer busts, returns False.
    """
    computer_player.adjust_for_ace()
    if (computer_player.sum_of_cards + computer_player.aces*11) > 21:
        if(computer_player.sum_of_cards + computer_player.aces*1) > 21:
            return True
        else:
            computer_player.sum = computer_player.sum_of_cards + computer_player.aces *1
            return False
    else:
        computer_player.sum = computer_player.sum_of_cards + computer_player.aces*11
        return False


def dealer_keeps_hitting():
    """
    Return True if deal can keep hitting, otherwise False
    """
    computer_player.adjust_for_ace()
    if (computer_player.sum_of_cards + computer_player.aces*11) > 17:
        if(computer_player.sum_of_cards + computer_player.aces*1) <= 17:
            return True
        else:
            return False
    else:
        return True


def dealer_wins():
    """
    Takes necessary action if dealer wins.
    """
    print("===========================")
    print("| Better luck next time ! |")
    print("===========================")
    new_chip.lose_bet()  # Bet deducted from player's total sum.
    print(f'Your total sum = {new_chip.total}$')


# Game play begins here.....
play_begins = True
while play_begins:
    clear_output(wait=False)
    # Game Opening
    print("========================")
    print("| Welcome To BlackJack |")
    print("========================")
    # After you enter inside a casino, first of all you buy chips.
    new_chip = Chips()

    # If game is continued, second game starts from here.
    play_again = True
    while play_again:
        new_deck = Deck()  # Creating a new deck of cards.
        new_deck.shuffle()  # Deck shuffled.

        # Ask for bet
        print(f'Total={new_chip.total}')
        take_bet()  # Take bet from player

        human_player = Hand()  # Human player created; Hand object.
        # This section is for dealing card to human player
        card_dealt_to_human_player = new_deck.deal()
        human_player.add_card(card_dealt_to_human_player)
        human_player.add_card(card_dealt_to_human_player)

        computer_player = Hand()  # Computer player created; Hand object.
        # This section is for dealing card to computer player
        card_dealt_to_computer = new_deck.deal()
        computer_player.add_card(card_dealt_to_computer)
        computer_player.add_card(card_dealt_to_computer)

        human_player.adjust_for_ace()
        computer_player.adjust_for_ace()

        # To Show Dealer's one card and player's both cards.
        show_some(player=human_player, dealer=computer_player)

        # Ask player if he wishes to hit or stand?
        human_playing = True
        dealer_turn = True
        while human_playing:
            human_playing = hit_or_stand(card_deck=new_deck, hand=human_player)
            if human_playing is True:
                # Before going for next hit; let the player check his card once more.
                show_some(player=human_player, dealer=computer_player)
                if player_busts() is True:
                    human_playing = False
                    show_all(player=human_player, dealer=computer_player)
                    dealer_wins()
                    dealer_turn = False
            else:
                # If player doesn't want more cards; sum all the cards.
                player_busts()

        # Once Human player stands; dealer's turn begins. This means human player hasn't busted yet.
        if dealer_turn is True:
            computer_playing = True
            while computer_playing:
                if dealer_keeps_hitting() is True:
                    hit(card_deck=new_deck, hand=computer_player)
                else:
                    computer_playing = False

            # checking wining condition
            if dealer_busts() is True:
                show_all(player=human_player, dealer=computer_player)
                player_wins()
            else:
                dealer_busts()  # To get the sum of dealer's card.
                # Compare the sum of cards; the player with sum nearest to 21 wins.
                if human_player.sum > computer_player.sum:
                    show_all(player=human_player, dealer=computer_player)
                    player_wins()
                elif computer_player.sum > human_player.sum:
                    show_all(player=human_player, dealer=computer_player)
                    dealer_wins()
                else:
                    print("Game Tied!")

        # Ask if they wanted to play again?
        ask_to_play = str(input("Would you like to play again? (Y/N)"))
        if ask_to_play.upper() != 'Y':
            print()
            play_again = False
        else:
            # Release memory
            del new_deck
            del human_player
            del computer_player

    # Ask if they really wanted to quit game?
    ask_to_quit = str(input("Are you sure to quit game? (Y/N)"))
    if ask_to_quit.upper() == 'Y':
        print("-----------------------")
        print("Thank You for playing.")
        play_begins = False
    else:
        # Release memory
        del new_chip
    # End of game
