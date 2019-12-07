import subprocess

a=subprocess.Popen(['pbpaste'],stdout=subprocess.PIPE)
print(a)