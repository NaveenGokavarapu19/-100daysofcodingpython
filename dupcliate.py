import os
import subprocess
import datetime as dt
import shutil
import time


def file_compress():
        while True:
            source_dir = "/home/naveen/testing"
            os.chdir("/home/naveen/testing")

            file_list = sorted(filter(os.path.isfile, os.listdir('.')), key=os.path.getmtime)
            file_list.remove("connect-log.log")

            files_to_be_appended = [file for file in file_list if "tar" not in file]
            print(len(file_list))
            files_to_moved = [ file for file in file_list if "tar"  in file]
            to_move_files = []
            try:
                time_stamp = files_to_be_appended[0].split(".")[2]
                for i in range(5):
                    to_move_files.append(files_to_be_appended[i])
                process = subprocess.run(["tar", "-czf", f"connnect-log.{time_stamp}.tar.gz", files_to_be_appended[0],
                                          files_to_be_appended[1],
                                          files_to_be_appended[2],
                                          files_to_be_appended[3], files_to_be_appended[4]], capture_output=True)
                for file_name in to_move_files:
                    os.remove(f"{file_name}")

                for file_name in files_to_moved:
                    shutil.move(os.path.join(source_dir, file_name), "/tmp")
            except IndexError:
                # left_file_list = os.listdir('.')
                # left_file_list.remove("connect-log.log")
                # shutil.move(os.path.join(source_dir, left_file_list[1]), "/tmp")
                time.sleep(5)

            else:

                print(len(to_move_files))

                print(files_to_be_appended)
                print(len(files_to_be_appended))
                time.sleep(2)

            finally:
                time.sleep(2)
















file_compress()



