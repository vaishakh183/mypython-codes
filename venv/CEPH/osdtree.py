#This script is to find all Hosts where all OSDs are down.
import json
import subprocess

def osdtreedump():
    subprocess.call(["sudo", "ceph", "osd", "tree", "-f", "json", "-o", "/tmp/osdtree.json"])
    return 0

def removeosd(host,osd):
    for osddrive in osd:
        print("Removing OSD "+ str(osddrive))
        subprocess.call(["sudo", "ceph", "auth","del", "osd."+str(osddrive)])
        subprocess.call(["sudo", "ceph", "osd", "rm", osddrive])
        subprocess.call(["sudo", "ceph", "osd", "crush", "rm", "osd."+str(osddrive)])
        print("OSD "+ str(osddrive) +" is removed.. from "+ str(host) )
    return 0


def main():
    OSDs=[]
    osdcount=0
    hosts=[]
    down_hosts={}
    with open("osdtree.json","r") as f:
        osdtree=json.load(f)
        for i in osdtree['nodes']:
            if i['type']=='host':
                osdcount=len(i['children'])
                hostname=i['name']
                downosds = 0
                OSDs=i['children']
            if osdcount > 0:
                for item in OSDs:
                    if item == i['id']:
                        if i['status'] =='down':
                            downosds +=1
                        if downosds == osdcount:
                            hosts.append(hostname)
                            down_hosts[hostname]=OSDs
    f.close()
    return down_hosts
if __name__=="__main__":
    osdtreedump()
    hosts=main()
    for i,j in hosts.items():
        print("Going to remove OSDs " +str(j) +" from " + i)
        removeosd(i,j)
