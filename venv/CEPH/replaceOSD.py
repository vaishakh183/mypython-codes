import psutil
import subprocess
import glob
import re
import json
import time
import os

def getdrives(drive_name):
    alldrives=[]
    drivelist=glob.glob("/dev/sd*")
    drivelist.sort()
    for i in drivelist:
        alldrives.append(i)
#    print(alldrives)
    if drive_name in alldrives:
        return 0
    else:
        return 1

#check ceph status
def ceph_status():
    #get ceph status
    subprocess.call(["sudo","ceph","status","-f","json","-o","/tmp/cephstatus"])
    with open("/tmp/cephstatus","r") as f:
        a=f.readline()
        file_json=json.loads(a)
        cephstatus=file_json['health']['status']
    f.close()
    subprocess.call(["sudo", "rm","-f","/tmp/cephstatus"])
    return cephstatus

def check_backfilling():
    #get pg dump
    count=0
    subprocess.call(["sudo","ceph","pg","dump","-f","json","-o","/tmp/pgstatus.json"])
    with open("/tmp/pgstatus.json","r") as f:
        data=json.loads(f)
        for pgs in data['pg_stats']:
            pg_state=pgs['state']
            if "backfilling" in pg_state:
                count +=1
    f.close()
    subprocess.call(["sudo", "rm","-f","/tmp/pgstatus.json"])
    return count

def add_new_drive_to_cluster(drive):
    print("Running ceph-disk prepare "+ str(drive))
    status=subprocess.call(["sudo","ceph-disk","prepare",str(drive)])
    if status == 0:
        print("ceph-disk prepare completed. ")
        subprocess.call(["sudo", "ceph-disk", "activate",str(drive)])
        print("ceph-disk activated.. ")


#remove OSD from CrushMap
def remove_osd_from_crushmap(osd_id):
    print("OSD ID is "+ str(osd_id))
    status=subprocess.call(["sudo","ceph","osd","find", str(osd_id)])
    if status !=0:
#        print("Removing ceph auth for the OSD "+str(osd_id))
#        subprocess.call(["sudo", "ceph", "auth", "del", "osd."+str(osd_id)])
#        print("Removing OSD...")
#        subprocess.call(["sudo", "ceph", "osd", "rm", str(osd_id)])
#        print("Removing OSD from Crush Map..")
#        subprocess.call(["sudo", "ceph", "osd", "crush", "rm","osd."+str(osd_id)])
        #check for backfilling
        backfill=check_backfilling()
        while backfill > 0:
            print(str(backfill)+ "pgs are backfilling...Will continue script after backfill completes.")
            time.sleep(60)
            backfill=check_backfilling()
        cephstatus=ceph_status()
        if backfill == 0 and cephstatus=="active+clean" or cephstatus=="HEALTH_WARN":
            #check /var/lib/ceph/osd exists
            if os.path.exists('/var/lib/ceph/osd'):
                #add new drive to cluster
                add_new_drive_to_cluster(drive)
    else:
        print("Unable to find OSD..")


def main():
    drive_name=input("Enter full path of new Drive in quotes. Example '/dev/sdx' ")
    ret=getdrives(drive_name)
    if ret == 0:
        print(drive_name + " is available")
        osd=input("Enter OSD ID")
        remove_osd_from_crushmap(osd)
#cephstatus=ceph_status()
#print(cephstatus)
#osd=1
#drive="/dev/sdd"
#remove_osd_from_crushmap(osd)
#add_new_drive_to_cluster(drive)
#    else:
#        print("Given Drive is not avialable..Check again..")


if __name__=="__main__":
    main()
