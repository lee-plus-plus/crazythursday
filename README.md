# crazythursday: your python REFUSE to work on Crazy Thursday

crazythursday is a library that allows you to go to KFC in time on Crazy Thursday by raising `CrazyThursdayException`. 

## Usage

```
from crazythursday import CrazyThursday

@CrazyThursday
def hello():
    print('hello')

if __name__ == '__main__':
    hello() # crazythursday.kfc.CrazyThursdayException: KFC Crazy Thursday WhoEver Gives me 50 CNY, I Will Thank Him.
```

