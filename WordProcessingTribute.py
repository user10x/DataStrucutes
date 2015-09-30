__author__ = 'nipchawla'
import os,re


inp=open("WordProcessor")
out=open("Output.txt","r+")
l=[]
p = re.compile('.?!')
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)

print matchObj.group()


print p.match("my name is nipun.")

print p.match("[^a-zA-Z0-9_]")

for eachline in inp:
    splitlines=eachline.split("\n")[0]
    tokenize=splitlines.splitlines()
    #print tokenize

inp.close()
out.close()
