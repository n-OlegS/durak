import random


class Card:
    def __init__(self, suit, rank, player=None):
        self.suit = suit
        self.rank = rank
        self.player = player

    @staticmethod
    def compare(c_1, c_2, trump):
        assert (c_1.suit == c_2.suit) or (c_1.suit == trump or c_2.suit == trump), 'жопа вам, а не compare'

        if c_1.rank > c_2.rank:
            return c_1

        return c_2

    def __str__(self):
        bukovkiandchiselski = {
            6: '6',
            7: '7',
            8: '8',
            9: '9',
            10: '10',
            11: 'J',
            12: 'Q',
            13: 'K',
            14: 'T'
        }

        return f'{self.suit}-{bukovkiandchiselski[self.rank]}'

#hello world