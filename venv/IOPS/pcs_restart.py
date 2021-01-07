import subprocess

def get_pid(process):
    try:
        PID=map(int,subprocess.check_output(["pidof", process]).split())
    except CalledProcessError:
        print("Process not running")
    return PID

def get_openfiles(processid):
    total=subprocess.Popen(["lsof","-p",processid],stdout=subprocess.PIPE,)
    count=subprocess.Popen(["wc","-l"],stdin=total.stdout,stdout=subprocess.PIPE)
    aa=count.stdout
    for i in aa:
        print(i.strip())
    return i.strip()

def pcs_restart():
    restart=subprocess.Popen(["pcs","resource","restart","LogService"],shell=True)
    try:
        restart.communicate()
    except:
        return 1

def main():
    PID=get_pid("rsyslogd")
    for processid in PID:
        openfiles=get_openfiles(processid)
        if int(openfiles) > 1000:
            pcs_restart()

if __name__=="__main__":
    main()


