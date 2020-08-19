import os
os.environ['ANSI_COLORS_DISABLED']="1"
import fire
def hi():
    print('Hi, I am wkmake.'.center(50,'*'))
def main():
    fire.Fire()

