import time
""" NOTE: epoch (pronounced 'epic') means the date from which computer began to measure time. epoch
is usually used as a reference point and this epoch depends on the OS """

print(time.ctime(0))  # prints epoch
print(time.ctime(2000000))  # converts the seconds to time from epoch

print(time.time())  # prints seconds since epoch to this point

print(time.ctime(time.time()))  # prints today's time and date

# other time methods can be studied from the python official documentation
