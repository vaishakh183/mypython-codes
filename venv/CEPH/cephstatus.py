import json
import subprocess

with open("cephstatus","r") as f:
    a=f.readline()
    b=json.loads(a)
    print(b['fsid'])
try:
    aa=subprocess.call(["sudo", "ceph", "osd", "find", str(osd_id)])
except aa.