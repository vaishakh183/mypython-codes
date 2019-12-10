import time
import os

def check_stat(log_file):
    for i in log_file:
        if os.path.isfile(str(i)):
            status = os.stat(i)
            modified_time = status.st_mtime
            current_time = time.time()
            time_diff_in_min = (int(current_time) - int(modified_time)) / 60
            hour = time_diff_in_min // 60
            minute = time_diff_in_min % 60
            return hour,minute
        else:
            print("Log file does not exist.")

log_file = ["/var/log/secure","/var/log/messages","/var/log/maillog","/var/log/nginx/access.log"]
hour,minute = check_stat(log_file)
print("File has not modified since " + str(hour) +" hours and " + str(minute)+ " minutes")
