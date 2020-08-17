"""
contains all files related to making animations
"""
import random

from asciimatics.exceptions import ResizeScreenError
from asciimatics.screen import Screen
from asciimatics.effects import Stars, Print
from asciimatics.particles import RingFirework, SerpentFirework, StarFirework, PalmFirework, Explosion
from asciimatics.renderers import SpeechBubble, Rainbow, StaticRenderer
from asciimatics.scene import Scene
import sys

_happy_birthday = """  .---.  .---.    ____    .-------. .-------.  ____     __    _______  .-./`) .-------. ,---------. .---.  .---.  ______        ____       ____     __
 |   |  |_ _|  .'  __ `. \  _(`)_ \\  _(`)_ \ \   \   /  /  \  ____  \\ .-.')|  _ _   \\          \|   |  |_ _| |    _ `''.  .'  __ `.    \   \   /  /
 |   |  ( ' ) /   '  \  \| (_ o._)|| (_ o._)|  \  _. /  '   | |    \ |/ `-' \| ( ' )  | `--.  ,---'|   |  ( ' ) | _ | ) _  \/   '  \  \    \  _. /  ' 
 |   '-(_{;}_)|___|  /  ||  (_,_) /|  (_,_) /   _( )_ .'    | |____/ / `-'`"`|(_ o _) /    |   \   |   '-(_{;}_)|( ''_'  ) ||___|  /  |     _( )_ .'  
 |      (_,_)    _.-`   ||   '-.-' |   '-.-'___(_ o _)'     |   _ _ '. .---. | (_,_).' __  :_ _:   |      (_,_) | . (_) `. |   _.-`   | ___(_ o _)'   
 | _ _--.   | .'   _    ||   |     |   |   |   |(_,_)'      |  ( ' )  \|   | |  |\ \  |  | (_I_)   | _ _--.   | |(_    ._) '.'   _    ||   |(_,_)'    
 |( ' ) |   | |  _( )_  ||   |     |   |   |   `-'  /       | (_{;}_) ||   | |  | \ `'   /(_(=)_)  |( ' ) |   | |  (_.\.' / |  _( )_  ||   `-'  /     
 (_{;}_)|   | \ (_ o _) //   )     /   )    \      /        |  (_,_)  /|   | |  |  \    /  (_I_)   (_{;}_)|   | |       .'  \ (_ o _) / \      /      
 '(_,_) '---'  '.(_,_).' `---'     `---'     `-..-'         /_______.' '---' ''-'   `'-'   '---'   '(_,_) '---' '-----'`     '.(_,_).'   `-..-'       """
_fass = """
 ________    ____       .-'''-.     .-''-.    .-_'''-.      ____     .---.  
|        | .'  __ `.   / _     \  .'_ _   \  '_( )_   \   .'  __ `.  \   /  
|   .----'/   '  \  \ (`' )/`--' / ( ` )   '|(_ o _)|  ' /   '  \  \ |   |  
|  _|____ |___|  /  |(_ o _).   . (_ o _)  |. (_,_)/___| |___|  /  |  \ /   
|_( )_   |   _.-`   | (_,_). '. |  (_,_)___||  |  .-----.   _.-`   |   v    
(_ o._)__|.'   _    |.---.  \  :'  \   .---.'  \  '-   .'.'   _    |  _ _   
|(_,_)    |  _( )_  |\    `-'  | \  `-'    / \  `-'`   | |  _( )_  | (_I_)  
|   |     \ (_ o _) / \       /   \       /   \        / \ (_ o _) /(_(=)_) 
'---'      '.(_,_).'   `-...-'     `'-..-'     `'-...-'   '.(_,_).'  (_I_)  
"""

fireworks = [
    (PalmFirework, 25, 30),
    (PalmFirework, 25, 30),
    (StarFirework, 25, 35),
    (StarFirework, 25, 35),
    (StarFirework, 25, 35),
    (RingFirework, 20, 30),
    (SerpentFirework, 30, 35),
]


class AsciiImage(StaticRenderer):
    """
    This class passes in text with all needed attributes to be processed by asciimatics
    """

    def __init__(self, text) -> None:
        """
        :param text: The text string to convert with Figlet.
        """
        super(AsciiImage, self).__init__()
        self._images = [text]


def blast(screen, quantity: int, blast_frame: int, x, y) -> StarFirework or RingFirework or SerpentFirework or \
                                                            PalmFirework:
    """
    yields many fireworks that will all be on the exact same trajectory and timing to make it create a massive blast
    :returns: a StarFirework, RingFirework, SerpentFirework or PalmFirework effect all on the same trajectory and time
    """
    for _ in range(quantity):
        firework, start, stop = random.choice(fireworks)
        yield firework(screen, x, y, 30, start_frame=blast_frame)


def append_fireworks(screen, duration: int) -> StarFirework or RingFirework or SerpentFirework or PalmFirework:
    """
    yields each firework that has to be added to the effects list
    :param screen: the asciimatics screen object
    :param duration: how long you want the fireworks to go on for
    :returns: a StarFirework, RingFirework, SerpentFirework or PalmFirework effect
    """
    width = screen.width
    height = screen.height
    height_range = (height // 8, height * 3 // 4)
    start_frame_range = duration * 5 // 2
    for _ in range(duration):
        firework, start, stop = random.choice(fireworks)
        x_axis = random.randint(0, width)
        y_axis = random.randint(height_range[0], height_range[1])
        yield firework(screen, x_axis, y_axis, random.randint(start, stop),
                       start_frame=random.randint(0, start_frame_range))


def happy_birthday_animation(screen, messages: list = None) -> None:
    """
    the happy birthday animation
    :param messages:
    :param screen:
    :return:
    """
    messages = messages if messages is not None else [
        {'message': _happy_birthday,
         'y-axis': screen.height // 2 - 12,
         'start': 100,
         'end': False,
         'effect': True},
        {'message': _fass,
         'y-axis': screen.height // 2 + 0,
         'start': 100,
         'end': False,
         'effect': True},
        {'message': 'long message long message long message \nlong message long message long message ',
         'y-axis': screen.height // 6 * 5,
         'start': 300,
         'end': 302,
         'effect': False},
        {'message': 'Press x to exit',
         'y-axis': screen.height // 8 * 7,
         'start': 500,
         'end': False,
         'effect': False},
    ]
    scenes = []
    effects = [
        Stars(screen, screen.width),
        Explosion(screen, x=screen.width // 2, y=screen.height // 2, life_time=100)
    ] + list(append_fireworks(screen, 10000))
    has_done_blast = False
    for message in messages:
        message['end'] = message['end'] if message['end'] is not False else 0
        if message['effect'] is True:
            effects.append(Print(screen, Rainbow(screen, AsciiImage(message['message'])), message['y-axis'],
                                 start_frame=message['start'], stop_frame=message['end']))
            if has_done_blast is False:
                effects += list(blast(screen, 10, message['start'] - 30, screen.width // 2, screen.height // 2))
                has_done_blast = True
        else:
            effects.append(Print(screen, SpeechBubble(message['message']), y=message['y-axis'],
                                 start_frame=message['start'], stop_frame=message['end']))
        if message.get("blast", False) is True:
            effects += list(blast(screen, 10, message['end'], screen.width // 2, message['y-axis']))

    scenes.append(Scene(effects, -1))
    screen.play(scenes, stop_on_resize=True)


def default_birthday_animation(screen) -> None:
    """
    the full animation thing
    """
    is_fass_birthday = random.choice([True, False])
    messages = [
        {'message': _happy_birthday,
         'y-axis': screen.height // 2 - 12,
         'start': 100,
         'end': False,
         'effect': True},
        {'message': _fass,
         'y-axis': screen.height // 2 + 0,
         'start': 100,
         'end': False,
         'effect': True},
        {'message': 'Happy birthday Fassey, I love you',
         'y-axis': screen.height // 6 * 5,
         'start': 300,
         'end': 310,
         'blast': True,
         'effect': False},
        {'message': 'Press x to exit',
         'y-axis': screen.height // 8 * 7,
         'start': 500,
         'end': False,
         'effect': False},
    ]
    if is_fass_birthday:
        happy_birthday_animation(screen, messages=messages)
    else:
        print("hello")


def run_default_birthday_animation() -> None:
    """
    Run the birthday animation
    :return:
    """
    try:
        Screen.wrapper(default_birthday_animation)
    except ResizeScreenError:
        run_default_birthday_animation()


if __name__ == '__main__':
    run_default_birthday_animation()
