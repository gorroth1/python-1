"""The amazing color module.

With all of the colors!
"""
base03 = '\033[1;30m'
base02 ='\033[0;30m'
base01 ='\033[1;32m'
base00 ='\033[1;33m'
base0 ='\033[1;34m'
base1 ='\033[1;36m' 
base2 ='\033[0;37m'
base3 ='\033[1;37m' 
cyan ='\033[0;36m'
violet ='\033[1;35m'
blue ='\033[0;34m' 
grey ='\033[1;32m'
red ='\033[0;31m'
reset ='\033[0m'
magenta ='\033[0;31m'
yellow ='\033[0;33m'
orange ='\033[1;31m'
green ='\033[0;32m'
clear ='\033[H\033[2J'

pink = magenta

import random
def random_color():
    return random.choice([yellow, orange, red, magenta, violet, blue, cyan, green])

def clear_screen():
    print(clear,end='')


if __name__ == '__main__':
    print(clear)
    print(grey + 'Grey' + reset)
    print(yellow + 'Yellow' + reset)
    print(orange + 'Orange' + reset)
    print(green + 'Green' + reset)
    print(pink + 'Pink' + reset)
    print(red + 'Red' + reset)
    print(blue + 'Blue' + reset)
    print(violet + 'Violet' + reset)
    print(cyan + 'Cyan' + reset)
    print(base3 + 'Base3' + reset)
    print(base2 + 'Base2' + reset)
    print(base1 + 'Base1' + reset)
    print(base0 + 'Base0' + reset)    
    print(base00 + 'Base00' + reset)
    print(base01 + 'Base01' + reset)
    print(base02 + 'Base02' + reset)
    print(base03 + 'Base03' + reset)
