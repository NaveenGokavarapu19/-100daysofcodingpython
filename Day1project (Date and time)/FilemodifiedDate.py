import os
import time

# Function to get the time at which file is modified


def get_modified_time(file_name):
    access_time = os.path.getatime(file_name)
    return access_time

# Function to convert epoch time to local time


def get_local_time(timestamp):
    local_time = time.ctime(timestamp)
    return local_time


# function to print the epoch time


def print_access_time_epoch (time_required):
    print("Last access time since the epoch:", time_required)

# Function to print the  local time


def print_access_time_local (local_time):
    print("Last access time :", local_time)


time_file_modified = get_modified_time("rfc3339time_stamp.py")
print_access_time_epoch(time_file_modified)
time_file_modified_local = get_local_time(time_file_modified)
print_access_time_local(time_file_modified_local)
