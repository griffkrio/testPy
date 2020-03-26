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
                import os.path, time
                dt1=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_Android.buildNumbers.properties')
                dt2=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_AndroidPredprod.buildNumbers.properties')
                dt3=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_AndroidPredprodX64.buildNumbers.properties')
                dt4=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_Android_Prod.buildNumbers.properties')
                dt5=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_AndroidProdX64.buildNumbers.properties')
                dt6=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_AndroidProdX86.buildNumbers.properties')
                dt7=('/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/HopaRenovation_Android_x64.buildNumbers.properties')
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat( dt1)
                dt1_a = mtime
                dt1_b = ctime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt2)
                dt2_a=ctime
                dt2_b=mtime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt3)
                dt3_a=ctime
                dt3_b=mtime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt4)
                dt4_a=ctime
                dt4_b=mtime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt5)
                dt5_a=ctime
                dt5_b=mtime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt6)
                dt6_a=ctime
                dt6_b=mtime
                (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(dt7)
                dt7_a=ctime
                dt7_b=mtime
                while dt1_a!=dt2_a:
                    if dt1_a!=dt2_a:
                        if dt1_a > dt2_a :
                            import shutil
                            shutil.copy(dt1, dt2)
                            break
                        elif dt2_a> dt1_a:
                            import shutil
                            shutil.copy(dt2,dt1)
                            break
                while dt1_b!=dt2_b:
                        if dt1_b>dt2_b:
                            import shutil
                            shutil.copy(dt1, dt2)
                            break
                        elif dt2_b>dt1_b:
                            import shutil
                            shutil.copy(dt2, dt1)
                            break
                while dt1_a!=dt3_a:
                    if dt1_a!=dt3_a:
                        if dt1_a > dt3_a :
                            import shutil
                            shutil.copy(dt1, dt3)
                            break
                        elif dt3_a> dt1_a:
                            import shutil
                            shutil.copy(dt3,dt1)
                            break
                while dt1_b!=dt3_b:
                        if dt1_b>dt3_b:
                            import shutil
                            shutil.copy(dt1, dt3)
                            break
                        elif dt3_b>dt1_b:
                            import shutil
                            shutil.copy(dt3, dt1)
                            break
                while dt1_a!=dt4_a:
                    if dt1_a!=dt4_a:
                        if dt1_a > dt4_a :
                            import shutil
                            shutil.copy(dt1, dt4)
                            break
                        elif dt4_a> dt1_a:
                            import shutil
                            shutil.copy(dt4,dt1)
                            break
                while dt1_b!=dt4_b:
                        if dt1_b>dt4_b:
                            import shutil
                            shutil.copy(dt1, dt4)
                            break
                        elif dt4_b>dt1_b:
                            import shutil
                            shutil.copy(dt4, dt1)
                            break 
                while dt1_a!=dt5_a:
                    if dt1_a!=dt5_a:
                        if dt1_a > dt5_a :
                            import shutil
                            shutil.copy(dt1, dt5)
                            break
                        elif dt5_a> dt1_a:
                            import shutil
                            shutil.copy(dt5,dt1)
                            break
                while dt1_b!=dt5_b:
                        if dt1_b>dt5_b:
                            import shutil
                            shutil.copy(dt1, dt5)
                            break
                        elif dt5_b>dt1_b:
                            import shutil
                            shutil.copy(dt5, dt1)
                            break
                while dt1_a!=dt6_a:
                    if dt1_a!=dt6_a:
                        if dt1_a > dt6_a :
                            import shutil
                            shutil.copy(dt1, dt6)
                            break
                        elif dt6_a> dt1_a:
                            import shutil
                            shutil.copy(dt6,dt1)
                            break
                while dt1_b!=dt6_b:
                        if dt1_b>dt6_b:
                            import shutil
                            shutil.copy(dt1, dt6)
                            break
                        elif dt6_b>dt1_b:
                            import shutil
                            shutil.copy(dt6, dt1)
                            break
                while dt1_a!=dt7_a:
                    if dt1_a!=dt7_a:
                        if dt1_a > dt7_a :
                            import shutil
                            shutil.copy(dt1, dt7)
                            break
                        elif dt7_a> dt1_a:
                            import shutil
                            shutil.copy(dt7,dt1)
                            break
                while dt1_b!=dt7_b:
                        if dt1_b>dt7_b:
                            import shutil
                            shutil.copy(dt1, dt7)
                            break
                        elif dt7_b>dt1_b:
                            import shutil
                            shutil.copy(dt7, dt1)
                            break    
                while dt2_a!=dt3_a:
                    if dt2_a!=dt3_a:
                        if dt2_a > dt3_a :
                            import shutil
                            shutil.copy(dt2, dt3)
                            break
                        elif dt3_a> dt2_a:
                            import shutil
                            shutil.copy(dt3,dt2)
                            break
                while dt2_b!=dt3_b:
                        if dt2_b>dt3_b:
                            import shutil
                            shutil.copy(dt2, dt3)
                            break
                        elif dt3_b>dt2_b:
                            import shutil
                            shutil.copy(dt3, dt2)
                            break
                while dt2_a!=dt4_a:
                    if dt2_a!=dt4_a:
                        if dt2_a > dt4_a :
                            import shutil
                            shutil.copy(dt2, dt4)
                            break
                        elif dt4_a> dt2_a:
                            import shutil
                            shutil.copy(dt4,dt2)
                            break
                while dt2_b!=dt4_b:
                        if dt2_b>dt4_b:
                            import shutil
                            shutil.copy(dt2, dt4)
                            break
                        elif dt4_b>dt2_b:
                            import shutil
                            shutil.copy(dt4, dt2)
                            break 
                while dt2_a!=dt5_a:
                    if dt2_a!=dt5_a:
                        if dt2_a > dt5_a :
                            import shutil
                            shutil.copy(dt2, dt5)
                            break
                        elif dt5_a> dt2_a:
                            import shutil
                            shutil.copy(dt5,dt2)
                            break
                while dt2_b!=dt5_b:
                        if dt2_b>dt5_b:
                            import shutil
                            shutil.copy(dt2, dt5)
                            break
                        elif dt5_b>dt2_b:
                            import shutil
                            shutil.copy(dt5, dt2)
                            break
                while dt2_a!=dt6_a:
                    if dt2_a!=dt6_a:
                        if dt2_a > dt6_a :
                            import shutil
                            shutil.copy(dt2, dt6)
                            break
                        elif dt6_a> dt2_a:
                            import shutil
                            shutil.copy(dt6,dt2)
                            break
                while dt2_b!=dt6_b:
                        if dt2_b>dt6_b:
                            import shutil
                            shutil.copy(dt2, dt6)
                            break
                        elif dt6_b>dt1_b:
                            import shutil
                            shutil.copy(dt6, dt2)
                            break
                while dt2_a!=dt7_a:
                    if dt2_a!=dt7_a:
                        if dt2_a > dt7_a :
                            import shutil
                            shutil.copy(dt2, dt7)
                            break
                        elif dt7_a> dt2_a:
                            import shutil
                            shutil.copy(dt7,dt2)
                            break
                while dt2_b!=dt7_b:
                        if dt2_b>dt7_b:
                            import shutil
                            shutil.copy(dt2, dt7)
                            break
                        elif dt7_b>dt2_b:
                            import shutil
                            shutil.copy(dt7, dt2)
                            break       
                while dt3_a!=dt4_a:
                    if dt3_a!=dt4_a:
                        if dt3_a > dt4_a :
                            import shutil
                            shutil.copy(dt3, dt4)
                            break
                        elif dt4_a> dt3_a:
                            import shutil
                            shutil.copy(dt4,dt3)
                            break
                while dt3_b!=dt4_b:
                        if dt3_b>dt4_b:
                            import shutil
                            shutil.copy(dt3, dt4)
                            break
                        elif dt4_b>dt3_b:
                            import shutil
                            shutil.copy(dt4, dt3)
                            break 
                while dt3_a!=dt5_a:
                    if dt3_a!=dt5_a:
                        if dt3_a > dt5_a :
                            import shutil
                            shutil.copy(dt3, dt5)
                            break
                        elif dt5_a> dt3_a:
                            import shutil
                            shutil.copy(dt5,dt3)
                            break
                while dt3_b!=dt5_b:
                        if dt3_b>dt5_b:
                            import shutil
                            shutil.copy(dt3, dt5)
                            break
                        elif dt5_b>dt3_b:
                            import shutil
                            shutil.copy(dt5, dt3)
                            break
                while dt3_a!=dt6_a:
                    if dt3_a!=dt6_a:
                        if dt3_a > dt6_a :
                            import shutil
                            shutil.copy(dt3, dt6)
                            break
                        elif dt6_a> dt3_a:
                            import shutil
                            shutil.copy(dt6,dt3)
                            break
                while dt3_b!=dt6_b:
                        if dt3_b>dt6_b:
                            import shutil
                            shutil.copy(dt3, dt6)
                            break
                        elif dt6_b>dt3_b:
                            import shutil
                            shutil.copy(dt6, dt3)
                            break
                while dt3_a!=dt7_a:
                    if dt3_a!=dt7_a:
                        if dt3_a > dt7_a :
                            import shutil
                            shutil.copy(dt3, dt7)
                            break
                        elif dt7_a> dt3_a:
                            import shutil
                            shutil.copy(dt7,dt3)
                            break
                while dt3_b!=dt7_b:
                        if dt3_b>dt7_b:
                            import shutil
                            shutil.copy(dt3, dt7)
                            break
                        elif dt7_b>dt3_b:
                            import shutil
                            shutil.copy(dt7, dt3)
                            break     
                while dt4_a!=dt5_a:
                    if dt4_a!=dt5_a:
                        if dt4_a > dt5_a :
                            import shutil
                            shutil.copy(dt4, dt5)
                            break
                        elif dt5_a> dt4_a:
                            import shutil
                            shutil.copy(dt5,dt4)
                            break
                while dt4_b!=dt5_b:
                        if dt4_b>dt5_b:
                            import shutil
                            shutil.copy(dt4, dt5)
                            break
                        elif dt5_b>dt4_b:
                            import shutil
                            shutil.copy(dt5, dt4)
                            break
                while dt4_a!=dt6_a:
                    if dt4_a!=dt6_a:
                        if dt3_a > dt6_a :
                            import shutil
                            shutil.copy(dt4, dt6)
                            break
                        elif dt6_a> dt4_a:
                            import shutil
                            shutil.copy(dt6,dt4)
                            break
                while dt4_b!=dt6_b:
                        if dt4_b>dt6_b:
                            import shutil
                            shutil.copy(dt4, dt6)
                            break
                        elif dt6_b>dt4_b:
                            import shutil
                            shutil.copy(dt6, dt4)
                            break
                while dt4_a!=dt7_a:
                    if dt4_a!=dt7_a:
                        if dt4_a > dt7_a :
                            import shutil
                            shutil.copy(dt4, dt7)
                            break
                        elif dt7_a> dt4_a:
                            import shutil
                            shutil.copy(dt7,dt4)
                            break
                while dt4_b!=dt7_b:
                        if dt4_b>dt7_b:
                            import shutil
                            shutil.copy(dt4, dt7)
                            break
                        elif dt7_b>dt4_b:
                            import shutil
                            shutil.copy(dt7, dt4)
                            break   
                while dt5_a!=dt6_a:
                    if dt5_a!=dt6_a:
                        if dt5_a > dt6_a :
                            import shutil
                            shutil.copy(dt5, dt6)
                            break
                        elif dt6_a> dt5_a:
                            import shutil
                            shutil.copy(dt6,dt5)
                            break
                while dt5_b!=dt6_b:
                        if dt5_b>dt6_b:
                            import shutil
                            shutil.copy(dt5, dt6)
                            break
                        elif dt6_b>dt5_b:
                            import shutil
                            shutil.copy(dt6, dt5)
                            break
                while dt5_a!=dt7_a:
                    if dt5_a!=dt7_a:
                        if dt5_a > dt7_a :
                            import shutil
                            shutil.copy(dt5, dt7)
                            break
                        elif dt7_a> dt5_a:
                            import shutil
                            shutil.copy(dt7,dt5)
                            break
                while dt5_b!=dt7_b:
                        if dt5_b>dt7_b:
                            import shutil
                            shutil.copy(dt5, dt7)
                            break
                        elif dt7_b>dt5_b:
                            import shutil
                            shutil.copy(dt7, dt5)
                            break                
                while dt6_a!=dt7_a:
                    if dt6_a!=dt7_a:
                        if dt6_a > dt7_a :
                            import shutil
                            shutil.copy(dt6, dt7)
                            break
                        elif dt7_a> dt6_a:
                            import shutil
                            shutil.copy(dt7,dt6)
                            break
                while dt6_b!=dt7_b:
                        if dt6_b>dt7_b:
                            import shutil
                            shutil.copy(dt6, dt7)
                            break
                        elif dt7_b>dt6_b:
                            import shutil
                            shutil.copy(dt7, dt6)
                            break                                                                
        _method_name.__name__ = "process_{}".format(method)
        setattr(cls, _method_name.__name__, _method_name)

    for method in EventProcessor._methods:
        process_generator(EventProcessor, method)

    watch_manager = pyinotify.WatchManager()
    event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

    watch_this = os.path.abspath("/root/.BuildServer/config/projects/HopaRenovation/buildNumbers/")
    watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
    event_notifier.loop()