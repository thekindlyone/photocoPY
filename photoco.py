import os, time, sys, shutil

def main():
    dir=os.getcwd()
    if len(sys.argv)>1:
        dir=sys.argv[-1]
    photos=filter(lambda x:os.path.splitext(x)[-1].lower() in ['.png','.jpg','.bmp','.jpeg'],os.listdir(dir))
    
    def copytodir(fn,d):
        rcode=1
        if not os.path.exists(d):
            try:
                os.makedirs(d)
                rcode=2
            except:
                rcode = sys.exc_info()[1]
        try: shutil.move(fn,d)
        except: rcode = sys.exc_info()[1]
        return rcode
    
    for photo in photos:
        photo=os.path.join(dir,photo)
        (mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime) = os.stat(photo)
        timeinfo= time.ctime(mtime).split(' ')
        newdirectory= os.path.join(dir,timeinfo[1]+' '+timeinfo[-1])
        rc=copytodir(photo,newdirectory)
        if rc==1: print photo ,' copied to dir ',newdirectory
        else:
            if rc==2: print photo ,'copied to dir ',newdirectory,'(created now)'
            else : print 'uh oh ',rc
         
    #print photos


if __name__ == '__main__':
  main()