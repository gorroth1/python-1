"""Welcome to the utils.py where you can grab all of your utilities"""
import colors as c

def ask(question):
    print(c.red + question + c.reset)
    answer = input('>' + c.base3).lower().strip()
    print(c.reset)
    return answer



if __name__ == '__main__':
    bruh = ask('Bruh')
    print(bruh)
