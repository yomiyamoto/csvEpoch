import os
import datetime
import time

path = 'C:\\Users\\ymiyamoto.MIS\\Desktop\\Camera 1'
files = os.listdir(path)
i = 1

for file in files:
    print(file)
    ts = time.strptime(file[0:file.find('.')], "%m-%d-%Y-%H-%M-%S")
    ts_string = str(time.mktime(ts))
    newname = ts_string[0:ts_string.find('.')]
    newfile = newname + '.mp4'
    print(newfile)
    os.rename(path + "\\" + file, path + "\\" + newfile)
    i = i+1