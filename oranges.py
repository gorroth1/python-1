
import colors as c
from utils import ask

intro = c.orange + '''
Welcome to the orange quiz game!!!!!!
'''  + c.reset 
 

def q1():   
    color = ask(c.yellow + 'What is the color of an orange?' + c.reset)
    if color == 'orange':
        return True
    print(c.red + 'You have failed' + c.reset)
    return False

def q2():
    peel = ask(c.green + 'What is the correct way to eat an orange?' + c.reset)
    if peel.startswith("peel"):
        return True
    print(c.red + "You have failed" + c.reset)
    return False


def q3():
    type = ask(c.blue + 'Am I refferring to the fruit or color?' + c.reset)
    if type == ("fruit"):
        return True
    print (c.red + 'You have failed' + c.reset)
    return False
questions = [q1,q2,q3]

