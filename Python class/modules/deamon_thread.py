# daemon thread is thread that runs in the background, not really important for program
# execution useful for garbage collection, waiting for input and other background tasks

import threading
import time


def timer():
    print()
    count = 0
    while True:
        time.sleep(1)
        count += 1
        print(f"Logged in for {count} seconds")


x = threading.Thread(target=timer, daemon=True)
x.start()

question = input("Do you wish to exit?")

print(x.isDaemon())
