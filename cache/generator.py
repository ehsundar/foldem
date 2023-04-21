from datetime import datetime
from itertools import combinations

from deck import cards
from judge import winner, PlayerCards


def generate():
    last_seen_first_card = ""
    last_seen_changed_at = datetime.now()

    for current_cards in combinations(reversed(cards), 7):
        if last_seen_first_card != (*current_cards[:2],):
            last_seen_first_card = (*current_cards[:2],)
            print(f"took {(datetime.now() - last_seen_changed_at).total_seconds()}")
            print(f"processing combinations: {last_seen_first_card}, X...", flush=True)
            last_seen_changed_at = datetime.now()

            filename = f"{current_cards[0][0]}{current_cards[0][1]}-{current_cards[1][0]}{current_cards[1][1]}.dat"
            f = open(f"foldem_cache/{filename}", "w")

        winners = winner(current_cards[:5], [PlayerCards(*current_cards[5:])])
        w = winners[0]
        mode = w[1]

        f.write(mode.serialize() + "\n")

    f.close()
