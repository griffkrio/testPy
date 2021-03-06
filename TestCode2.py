import os
import pyinotify
while True:
    class EventProcessor(pyinotify.ProcessEvent):
        _methods = ["IN_CREATE",
                    "IN_ATTRIB",
                    "IN_DELETE",
                    "IN_MODIFY",
                    "IN_UNMOUNT",
                    "IN_DELETE_SELF",
                    "IN_MOVE_SELF",
                    "IN_MOVED_FROM",
                    "IN_UNMOUNT",]

    def process_generator(cls,method):
        def _method_name(self, event):
            print("Method name: process_{}()\n"
                "Path name: {}\n"
                "Event Name: {}\n".format(methodmethod, event.pathname, event.maskname))
            import time
            time.sleep(5)  
            if method :
                import os
                import os.path
                a=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build1Test.buildNumbers.properties')
                b=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build2Test.buildNumbers.properties')
                d=('/home/kriogen/git/testPy/notification/TestBuild1_Repotester_Build3Test.buildNumbers .properties')
                def MyFunk (x):
                    with open(x) as file:
                        lst = list()
                        for line in file.readlines(): 
                            lst.extend(line.rstrip().split(' '))
                    l_a= lst[-1]
                    a = l_a
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
                    lts_int=int(lts)
                    return(lts_int)
                    k=MyFunk(a)
                    f=MyFunk(b)
                    g=MyFunk(d)
                    r=(k,f,g)
                    h=max(r)
                    h_str=str(h)
                    dtr=("next.build=" + h_str)
                    a=open(a,"w")
                    a.write(dtr)
                    a.close()
                    b=open(b,"w")
                    b.write(dtr)
                    b.close()
                    d=open(d,"w")
                    d.write(dtr)
                    d.close()                                            
        _method_name.__name__ = "process_{}".format(method)
        setattr(cls, _method_name.__name__, _method_name)

    for method in EventProcessor._methods:
        process_generator(EventProcessor, method)

    watch_manager = pyinotify.WatchManager()
    event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

    watch_this = os.path.abspath("/home/kriogen/git/testPy/notification/")
    watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
    event_notifier.loop()