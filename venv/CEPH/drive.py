import psutil
import os
import glob
drives=psutil.disk_partitions()
for i in drives:
    print(i.device)


