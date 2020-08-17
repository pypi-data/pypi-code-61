"""
You won't read this but happy birthday

"""
import datetime
import random

import click
from pyfiglet import Figlet


from . import data
from . import bible

fonts = ['3-d', 'alligator', 'alphabet', 'catwalk', 'cosmic', 'doom', 'epic', 'isometric3', 'poison', 'speed']
f = Figlet(font=random.choice(fonts), width=150)


fasega_birthday = datetime.datetime(1998, 8, 18)

today = datetime.datetime.today()

if today.month <= fasega_birthday.month or (today.month <= fasega_birthday.month and today.day <= fasega_birthday.day):
    next_birthday = datetime.datetime(today.year, fasega_birthday.month, fasega_birthday.day)
else:
    next_birthday = datetime.datetime(today.year + 1, fasega_birthday.month, fasega_birthday.day)

until_next_birthday = next_birthday - today


def today_print():
    """
    Based on the day, decide what to print out
    :return:
    """
    if today.day == fasega_birthday.day and today.month == fasega_birthday.month:
        from . import birthdayAnimation
        birthdayAnimation.run_default_birthday_animation()
        return "Happy birthday Xx"
    else:
        return str(until_next_birthday)[:-7]


@click.command()
def cli() -> None:
    """
    \b
    A command line tool to interact with different part of elmer
    This include run details
    """
    click.echo("Hi Fass")
    click.secho(f'{f.renderText(today_print())}', fg="bright_red")
    click.secho(f'Affirmation:\n{data.get_random_affirmation()}', fg="bright_green")
    verse = bible.get_bible_verse()
    click.secho(f'book: {verse.book}\tchapter: {verse.chapter}\tverse no: {verse.verse_number}', fg="magenta")
    for version, scripture in verse.verse.items():
        click.secho(f'version: {version}\n  {scripture}', fg="bright_magenta")
