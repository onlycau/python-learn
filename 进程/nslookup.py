import subprocess 

#communicate()输入
print('$nslookup')
p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
output,err=p.communicate(b'set q=mx\python.org\nexit\n')
print('Exit code:',p.returncode)