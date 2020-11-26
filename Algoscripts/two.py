from subprocess import PIPE,Popen,STDOUT,run
p = run(['python', 'one.py'], stdout=PIPE,input='10\n20\nHello\nWorld', encoding='ascii')
print(p.stdout)