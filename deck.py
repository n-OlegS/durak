from card import Card
import random


class Deck:
    def __init__(self):
        self.deck = []

        for suit in ("♠", "♥", "♦", "♣"):
            for rank in range(6, 15):
                self.deck.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self, num):
        return [self.deck.pop(random.randrange(0, len(self.deck))) for _ in range(num)]


deck = Deck()
deck.deck = [1, 2, 3, 4, 5]
print(deck.deal(2))