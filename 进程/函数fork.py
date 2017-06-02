import os

print('Process (%s) start...' % os.getpid())#取得进程id
# Only works on Unix/Linux/Mac:
pid = os.fork()#fork（）调用一次 返回两次
if pid == 0:
    print('I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid()))
else:
    print('I (%s) just created a child process (%s).' % (os.getpid(), pid))