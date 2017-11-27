# 子进程

import subprocess

print('$ nslookup www.python.org')

r=subprocess.call(['nslookup','www.python.org'])
print('Exit code:',r)

# 子进程如果还需要输入,则可以通过communicate()方法输入
print('$ nslookup')

p=subprocess.Popen(['nslookup'],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE)

output,err=p.communicate(b'set q=mx\npython.org\nexit\n')

print(output)
print('Exit code:',p.returncode)
