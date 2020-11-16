import random
from collections import Counter


def can_be_palindrome(sequence):
    counts = Counter(sequence)
    odds = 0
    for count in counts.values():
        if count % 2:
            odds += 1
        if odds > 1:
            return False
    return True


def create_palindrome(sequence):
    counts = Counter(sequence)
    center = []
    left_sequence = []
    for item, count in counts.items():
        if count % 2:
            center += [item] * count
        else:
            left_sequence.append(item * int((count / 2)))
    right_sequence = list(reversed(left_sequence))
    return left_sequence + center + right_sequence


def activate(sequence):
    palindrome = "".join(create_palindrome(sequence))
    print(f"From the selected stack [{sequence}] a bridge is constructed:\n\t{palindrome}.")
    if is_palindrome(palindrome):
        print("The bridge is stable!")
    else:
        print("The bridge is unstable and collapses!")
    print()
    return


def is_palindrome(sequence):
    return sequence == sequence[::-1]


def stacks():
    while True:
        yield "".join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(random.randint(7, 13)))
