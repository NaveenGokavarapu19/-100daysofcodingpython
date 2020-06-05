import os
import  time

access_time = os.path.getatime("rfc3339time_stamp.py")
local_time = time.ctime(access_time)
print("Last access time since the epoch:", access_time)
print("Last access time(Local time):", local_time)
