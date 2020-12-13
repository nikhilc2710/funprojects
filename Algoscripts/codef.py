import sys
arr=set()
keys=0
lookup={}
import sys 


for line in sys.stdin: 
	if 'q' == line.strip(): 
		break
	print(f'Input : {line}') 

print("Exit") 


# sys.stdout.write('BLANK KEYS:{}\n'.format(keys-len(arr)))
# sys.stdout.write('TOTAL KEYS:{}\n'.format(keys))
# sys.stdout.write('NUMBER OF  LOCKS:{}\n'.format(len(arr)))