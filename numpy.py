#!/usr/bin/python3
'''Assignments :-
a.Take dimensionals from user and create a numpy array with random number as element
b. save the above output in a file
c. take or read numpy data from a file as done in  2 nd program and multiply by 6 and print it back
d.split the array into all possible outputs'''
#ans a,b,c,d
import numpy as np
#ans a
[a,b] = input("enter the dimensions")
arr = np.random.randint(int(a),int(b))
#ans b
np.save("file1.npy",arr)
#ans c
a2 = np.load('file1.npy','w+')
a2 *= 6
a4 = np.save('file1.npy',a2)
#ans d
a1=([2,4])
for i in a1:
 c =  np.split(arr,i)
 print(c)  
