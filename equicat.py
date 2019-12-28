#!/usr/bin/python3

file_name = input(" ")
f = open(file_name,'r')
t=f.read()
print(t)
f.close()
