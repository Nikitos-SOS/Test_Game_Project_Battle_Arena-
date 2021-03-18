import sys
import time

def typing(lst):
    for character in lst:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    print("")