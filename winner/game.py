class PlayerCards:
    def __init__(self, card_1, card_2):
        self.cards = (card_1, card_2)

    def __str__(self):
        return f"{self.cards}"

    def __repr__(self):
        return self.__str__()


class CommunityCards:
    def __init__(self, *cards):
        self.cards = cards

    def __str__(self):
        return f"{self.cards}"

    def __repr__(self):
        return self.__str__()
