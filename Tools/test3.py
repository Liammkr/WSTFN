import pydirectinput
import time
time.sleep(2)
i =10
while i > 0:
    pydirectinput.moveRel(0, 1000, relative=True)
    i-=1