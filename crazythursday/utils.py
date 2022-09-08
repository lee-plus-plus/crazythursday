from datetime import datetime
from freezegun import freeze_time

def is_crazy_thursday():
    return datetime.now().weekday() == 3

def just_crazy():
    freezer = freeze_time("2022-09-08 00:00:01", tick=True)
    freezer.start()
    
def stop_crazy():
    raise NotImplementedError("You Cannot Stop Crazy.")
    freezer.stop()