from harmony import RoyalFlush, StraightFlush, FourOfAKind, ThreeOfAKind, OnePair


class PlayerCards:
    def __init__(self, card_1, card_2):
        self.cards = (card_1, card_2)

    def __str__(self):
        return f"{self.cards}"


class CommunityCards:
    def __init__(self, *cards):
        self.cards = cards

    def __str__(self):
        return f"{self.cards}"


def main():
    p1 = PlayerCards(("4", "S"), ("6", "C"))
    p2 = PlayerCards(("4", "D"), ("K", "H"))

    com = CommunityCards(("4", "D"), ("J", "H"), ("A", "S"), ("T", "S"), ("2", "C"))

    for mode in (RoyalFlush, StraightFlush, FourOfAKind, ThreeOfAKind, OnePair):
        mode_p1 = mode((*com.cards, *p1.cards))
        mode_p2 = mode((*com.cards, *p2.cards))

        if mode_p1.applies() and not mode_p2.applies():
            print(f"player 1 wins: {mode_p1}")

        if not mode_p1.applies() and mode_p2.applies():
            print(f"player 2 wins: {mode_p2}")

        if mode_p1.applies() and mode_p2.applies():
            if mode_p1 == mode_p2:
                print(f"tie")
            elif mode_p1 > mode_p2:
                print(f"player 1 wins: {mode_p1}")
            else:
                print(f"player 2 wins: {mode_p2}")


if __name__ == '__main__':
    main()
