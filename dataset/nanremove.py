import os
files=os.listdir('.\Scraps')
for file in files:
    f=open(".\Scraps\{f}".format(f=file),"r")
    cont=f.read()
    f.close()
    cont=cont.replace("nan",'0')
    fn=open(".\Scraps\{f}".format(f=file),"w")
    fn.write(cont)
    fn.close()
files=os.listdir('.\Split')
for file in files:
    f=open(".\Split\{f}".format(f=file),"r")
    cont=f.read()
    f.close()
    cont=cont.replace("nan","0")
    fn=open(".\Split\{f}".format(f=file),"w")
    fn.write(cont)
    fn.close()
