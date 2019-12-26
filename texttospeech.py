#!/usr/bin/python3
#i = []
'''for n in open('/home/abhilashaopgautam/samplefile.txt','r'):
 total=0
 if n.strip():
  k = int(n)
  for i in k:
   total = total+i
print(total) 
n = open('/home/abhilashaopgautam/samplefile.txt','r').readlines()
total=0
for i in n:
  j =map(float,i)
  total = total + j
print(total)'''
import pyttsx3
a = open('run.txt','w+')
for j in range(10):
  a.write("%d\r\n"%j)
a.close()  
n = open('run.txt','r').readlines()
total=0
#k = n.readlines()
for i in n:
  j = float(i)
  total = total + j
print(total)                            
aa = pyttsx3.init()
aa.say("output is%d"%total)
aa.runAndWait()
