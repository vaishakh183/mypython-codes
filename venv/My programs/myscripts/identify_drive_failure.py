#Check drive errors.
#Version 1.0.0
import os
l1=[]
unique=[]
def drive_failure():
    f=open("dmesg","r")
    for lines in f:
        if "critical medium error" in lines:
            l1.append(lines.split(",")[1])
    unique = list(set(l1))
    f.close()
    return unique

#if os.geteuid() == 0:
drives=drive_failure()
for i in drives:
    print(str(i).upper() +" has critical errors. Its recomended to replace drive")
#else:
#    print("Please run as root user")
