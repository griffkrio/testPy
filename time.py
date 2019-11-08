import os
import pyinotify
class EventProcessors(pyinotify.ProcessEvent)
    _methods= ["IN_CREATE",
                "IN_MODIFY",]
def process_generator(cls, method):
    def _method_name(self, event):
        print("Method name: process_{}()\n"
               "Path name: {}\n"
               "Event Name: {}\n".format(method, event.pathname, event.maskname))
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)

for method in EventProcessor._methods:
    process_generator(EventProcessor, method)

watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

watch_this = os.path.abspath("/home/creativetrendadmin/git/testPy/notification")
watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
event_notifier.loop()
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/pythonTEst/TestBuild1.txt')
a=mtime
b=ctime
import os.path, time
(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat('/home/creativetrendadmin/pythonTEst/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
c=mtime
d=ctime
print(a,b,c,d)
