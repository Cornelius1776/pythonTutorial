""" In python the flow of prorams is one (thread) at a time, this is due to the glogal interpreter 
lock (GIL). For CPU intensive operations(internal events), the interpreter uses multiprocessing. 
For external events(web scraping, etc) the interpreter uses multitreading.  """
import threading
import time


def hi(name):
    print(f"Hi {name}")


def greet():
    time.sleep(2)
    print("I have greeted the neighbours")


def eat():
    time.sleep(5)
    print("Done eating")


def write_code():
    time.sleep(15)
    print("finished writing some programs")


# This will wait for one execution at a time, delaying others
""" greet()
eat()
write_code() """


# threading.Thread() places all the events on the main thread at the same time to allow the execute
# at their own pace.
a = threading.Thread(target=greet, args=())
a.start()

b = threading.Thread(target=eat, args=())
b.start()

c = threading.Thread(target=write_code, args=())
c.start()

# join() synchronises the output on the main thread
a.join()
b.join()
c.join()

hi("Cornelius")

print(threading.active_count())
print(threading.enumerate)
