import time;  # This is required to include time module.

ticks = time.time()
print("Number of ticks since 12:00am, July 24, 2018:", ticks)

# getting current time
import time;

localtime = time.localtime(time.time())
print("Local current time :", localtime)
# getting formatted time
import time;

localtime = time.asctime( time.localtime(time.time()) )
print( "Local current time :", localtime)