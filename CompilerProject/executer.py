# import subprocess
# cmd = 'go run helloworld.go '

# p = subprocess.Popen(cmd, stdout=subprocess.PIPE, shell=True)
# out, err = p.communicate() 
# result = out.decode('ascii')
# print(result)
a='''3 3
1 2 3
4 5 6
7 8 9
3
3 3
2 3
5,6
'''
import subprocess

child = subprocess.Popen(['python','program.py'], stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, shell=False)
a=child.communicate(a.strip().encode(),timeout=7)
print(a)
