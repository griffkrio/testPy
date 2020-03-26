import os.path
d=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build1Test.buildNumbers.properties')
c=open(d)
a=d.find("NextBuild=")
print(int(a))
c.close()
