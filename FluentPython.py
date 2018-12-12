import collections
from random import choice


Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for rank in self.ranks for suit in self.suits]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


suit_value = dict(spades=3, hearts=2, clubs=2, diamonds=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value*len(suit_value) + suit_value[card.suit]


a = "a！"
b = "a！"


# print('a' * 20 is 'aaaaaaaaaaaaaaaaaaaa', 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa')


*unknown, a, b = range(10)

print(unknown)
print('{:15}'|'1')