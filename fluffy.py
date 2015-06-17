
import colors as c
from utils import ask

intro = c.pink + '''
Welcome to the pink fluffy
unicorns quiz game!!!!!!
'''  + c.reset 

def q1():   
    fur = ask(c.orange + 'What is the color of a pink fluffy unicorns fur?' + c.reset)
    if fur == 'pink':
        return True
    return False

def q2():
    dance = ask(c.green + 'What do pink fluffy unicorns dance on?' + c.reset)
    if dance.startswith("rainbow"):
        return True
    return False


def q3():
    texture = ask(c.blue + 'Please use one word to describe the texture of their magical fur?' + c.reset)
    if texture.startswith("smile"):
        return True
    return False
questions = [q1,q2,q3]

