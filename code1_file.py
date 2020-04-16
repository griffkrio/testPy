import os
import os.path
d=open ('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build3Test.buildNumbers .properties','r' )
d=d.readline(15)
print(d)
d=d.find("next.build=")
print (str(d))
print(d)