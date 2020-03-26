import os
import os.path
d=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build1Test.buildNumbers.properties')
d= open(d)
d= d.read()
print (d)
d=d.find('next.build')
print(d)
d=d+2
print (d)
