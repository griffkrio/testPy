import os
import pyinotify
while True:
    class EventProcessor(pyinotify.ProcessEvent):
        _methods = ["IN_CREATE",
                    "IN_ATTRIB",
                    "IN_DELETE",
                    "IN_MODIFY",
                    "IN_UNMOUNT",]

    def process_generator(cls, method):
        def _method_name(self, event):
            print("Method name: process_{}()\n"
                "Path name: {}\n"
                "Event Name: {}\n".format(method, event.pathname, event.maskname))
        if method :
            import os.path, time
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/git/testPy/notification/TestBuild1.txt')
            a = mtime
            b = ctime
            import os.path, time
            (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
            c=ctime
            d=mtime
            while a!=d:
                if a!=d:
                    if a > d :
                        import shutil
                        shutil.copy('/home/creativetrendadmin/git/testPy/notification/TestBuild1.txt', '/home/creativetrendadmin/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
                        break
                    elif d > a:
                        import shutil
                        shutil.copy('/home/creativetrendadmin/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties','/home/creativetrendadmin/git/testPy/notification/TestBuild1.txt')
                        break
            while b!=c:
                    if b>c:
                        import shutil
                        shutil.copy('/home/creativetrendadmin/git/testPy/notification/TestBuild1.txt', '/home/creativetrendadmin/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
                        break
                    elif c>b:
                        import shutil
                        shutil.copy('/home/creativetrendadmin/git/testPy/notification/TestBuild1.txt', '/home/creativetrendadmin/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
                        break
        _method_name.__name__ = "process_{}".format(method)
        setattr(cls, _method_name.__name__, _method_name)

    for method in EventProcessor._methods:
        process_generator(EventProcessor, method)

    watch_manager = pyinotify.WatchManager()
    event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

    watch_this = os.path.abspath("/home/creativetrendadmin/git/testPy/notification")
    watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
    event_notifier.loop()