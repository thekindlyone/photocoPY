import os, time, sys, shutil
def copytodir(fn):
    timeinfo= time.ctime(os.stat(fn).st_mtime).split(' ')
    newdir= os.path.join(os.path.dirname(fn),timeinfo[1]+' '+timeinfo[-1])
    rc=1
    if not os.path.exists(newdir):
        try:
            os.makedirs(newdir)
            rc=2
        except:
            rc = sys.exc_info()[1]
    try: shutil.move(fn,newdir)
    except: rc = sys.exc_info()[1]
    if rc==1: print fn ,' copied to dir ',newdir
    else:
        if rc==2: print fn ,'copied to dir ',newdir,'(created now)'
        else : print 'uh oh ',rc
    return rc
    
if __name__ == '__main__':
    dir=os.getcwd()
    if len(sys.argv)>1: dir=sys.argv[-1]
    log=map(copytodir,(os.path.join(dir,each) for each in os.listdir(dir) if os.path.splitext(each)[-1].lower() in ['.png','.jpg','.bmp','.jpeg']))
