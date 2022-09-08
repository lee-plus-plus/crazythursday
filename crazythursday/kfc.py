from .utils import is_crazy_thursday

class CrazyThursdayException(Exception):
    def __init__(self, money=50):
        self.money = money
    def __str__(self):
        return "KFC Crazy Thursday WhoEver Gives me {} CNY, I Will Thank Him.".format(self.money)

def CrazyThursday(func):
    def wrapper():
        if is_crazy_thursday():
            raise CrazyThursdayException
        return func()
    return wrapper

