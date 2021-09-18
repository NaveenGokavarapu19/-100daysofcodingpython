import os
import subprocess
import datetime as dt
import shutil
import time

LOGS_PATH = "/home/naveen/testing"
DESTINATION = "/tmp/logs"


def change_to_current_path(to_change_path):
    """
    Function to change to required Directory
    :param to_change_path: PLease change LOGS_PATH variable to change the path
    :return: no return
    """
    os.chdir(to_change_path)


def get_file_list_without_current_log():
    """
    Lists the files created with earliest files created first as list
    Removing current log file from the list
    :return:
    """
    full_list = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
    full_list.remove("connect-log.log")
    return full_list


def filter_list(to_process_list):
    """
    Filter files according to the extension and appending them to there respective lists
    :param to_process_list:
    :return: tuple of  lists which contains names of log files and tar files
    """
    log_file_list = [file for file in to_process_list if "tar" not in file]
    tar_file_list = [file for file in to_process_list if "tar" in file]
    return log_file_list, tar_file_list


def compress_files(time_stamp, files_to_be_appended):
    """
    Using subprocess module to run tar command to tar first 5 files in the list
    Note: Tar file has limitation regarding naming. Only time-stamp with four divisions are accepted
    Note1: To debug print the process variable
    :param time_stamp: can be generated using datetime module with method datetime.datetime.now()
    :param files_to_be_appended:
    :return: no return
    """
    process = subprocess.run(["tar", "-czf", f"connect-log.{time_stamp}.tar.gz", files_to_be_appended[0],
                              files_to_be_appended[1],
                              files_to_be_appended[2],
                              files_to_be_appended[3], files_to_be_appended[4]], capture_output=True)


def remove_current_logs_and_mv_comp_files(to_move_files, files_to_be_moved):
    """
    moves tar files to specified location and removes source files
    :param to_move_files:
    :param files_to_be_moved:
    :return: no return
    """
    [os.remove(f"{file_name}") for file_name in to_move_files]
    [shutil.move(os.path.join(LOGS_PATH, file_name), DESTINATION) for file_name in files_to_be_moved]


def compress_logs():
    while True:
        change_to_current_path(LOGS_PATH)
        file_list = get_file_list_without_current_log()
        files_to_be_appended, files_to_be_moved = filter_list(file_list)
        print(files_to_be_moved)

        try:
            time_stamp = files_to_be_appended[0].split(".")[2]
            to_move_files = [files_to_be_appended[i] for i in range(5)]
            compress_files(time_stamp, files_to_be_appended)
            remove_current_logs_and_mv_comp_files(to_move_files, files_to_be_moved)


        except Exception:

            time.sleep(5)
            print("Hello")

        try:
            [shutil.move(os.path.join(LOGS_PATH, file_name), DESTINATION) for file_name in files_to_be_moved]

        except:
            time.sleep(1)

        else:
            time.sleep(2)

        finally:
            time.sleep(1)


compress_logs()
