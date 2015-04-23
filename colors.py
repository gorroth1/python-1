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
cyan='\033[0;36m'
violet='\033[1;35m'
blue='\033[0;34m' 
grey='\033[1;32m'
red='\033[0;31m'
reset='\033[0m'
magenta='\033[0;31m'
yellow='\033[0;33m'
orange='\033[1;31m'
green='\033[0;32m'
clear='\033[H\033[2J'

pink = magenta

if __name__ == '__main__':
    print(clear)
    print(grey + 'Grey' + reset)
    print(yellow + 'Yellow' + reset)
    print(orange + 'Orange' + reset)

