# importing modules
import itertools
import random


# class for shuffling and distributing cards
class ShuffleDistCards:
    def __init__(self, no_of_players):
        """ Initializing all require var
        Arg:
        no_of_players - Total number of player playing
        Returns:
        Dictionary of players as a key and his cards list as value
        """
        self.no_of_cards = 52
        self.no_of_players = no_of_players
        self.deck = []
        self.card_dist_dict = {}

    def create_n_shuffle_deck(self):
        # make a deck of cards
        self.deck = list(itertools.product(range(1, 14), ['Spade', 'Heart', 'Diamond', 'Club']))
        # shuffle the cards
        random.shuffle(self.deck)

    def dist_cards(self):
        # Distribute cards among all the players
        for num in range(0, self.no_of_players):
            key = 'player_' + str(num + 1)
            self.card_dist_dict[key] = [self.deck[i] for i in list(range(num, self.no_of_cards, self.no_of_players))]
        return self.card_dist_dict
