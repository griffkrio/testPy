
    while True:
    import os.path, time
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/pythonTEst/TestBuild1.txt')
    a=mtime
    b=ctime
    import os.path, time
    (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
    c=ctime
    d=mtime
    while a!=d:
            if a!=d:
                if a > d :
                    import shutil
                    shutil.copy('/home/creativetrendadmin/pythonTEst/TestBuild1.txt', '/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
                    break
                elif d > a:
                    import shutil
                    shutil.copy('/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties','/home/creativetrendadmin/pythonTEst/TestBuild1.txt')
                    break
    while b!=c:
        if b>c:
            import shutil
            shutil.copy('/home/creativetrendadmin/pythonTEst/TestBuild1.txt', '/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
            break
        elif c>b:
            import shutil
            shutil.copy('/home/creativetrendadmin/pythonTEst/TestBuild1.txt', '/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
            break