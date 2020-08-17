"""
Stored data
"""
from pathlib import Path
import random

affirmation_file = Path(__file__).parent / 'affirmations.txt'


def get_random_affirmation():
    """
    From all the affirmations in the txt file, return a random affirmation
    :return:
    """
    with affirmation_file.open('r') as affirmations:
        affirmation_list = []
        for affirmation in affirmations:
            affirmation_list.append(affirmation)

    return affirmation_list[random.randint(0, len(affirmation_list) - 1)]
