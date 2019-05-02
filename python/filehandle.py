#read, write,append, r+, w+, a+
import time
#file=open('samplefile.txt','w+')
#file=open('samplefile.txt','r')
#file=open('samplefile.txt','a')
#file.write('piyush pande '+time.ctime())
#file.write('shehal\n')
#file.write('narayani\n')
#file.close()

#file=open('samplefile.txt','r+')
#file=open('samplefile.txt','r')
#file=open('samplefile.txt','a')
#file.write('piyush pande\n')
#print(file.seek(0))
#print(file.read())
#file.close()
#file=open('samplefile.txt','a')
#file.write('shehal Thakur\n')
#file.close()

file=open('samplefile3.txt','xb')
file.write('Python File')
file.close()
file=open('samplefile3.txt')
new_file=file
print(new_file.read())
