import random


class Queue:
    """A first-in, first-out (FIFO) queue of customer entries."""

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        # add a new entry to the back of the line
        self.items.append(item)

    def dequeue(self):
        # remove and return the entry at the front of the line
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        # look at the front entry without removing it
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """Pick a random winner, then dequeue everyone up to and including them."""
        if self.is_empty():
            print("No entries in the raffle.")
            return None

        # choose a random position in the line
        winner_index = random.randint(0, len(self.items) - 1)
        winner = self.items[winner_index]

        # remove entries from the front until the winner has been removed
        for _ in range(winner_index + 1):
            self.dequeue()

        print(f"The winner is: {winner}")
        return winner