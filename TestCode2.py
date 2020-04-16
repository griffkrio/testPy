import os
import os.path
a=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build1Test.buildNumbers.properties')

with open(a) as file:
    lst = list()
    for line in file.readlines(): 
        lst.extend(line.rstrip().split(' '))
lt= lst[-1]
a = lt
spisok = []
Num = ''
for c in a:
    if '0' <= c <= '9':
        Num = Num + c
    else:
        if Num != '':
            spisok.append(Num)
            Num = ''
if Num != '':
    spisok.append(Num)
lts=spisok[-1]
print (lts)
lts_int= int(lts)
trt=lts_int + 20
print (trt)
trt_str=str(trt)
dtr=str("next.build=" + trt_str)
print (dtr)
at=open("/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build1Test.buildNumbers.properties", "w")
at.write(str(dtr))
at.close()